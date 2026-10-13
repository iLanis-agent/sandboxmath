import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

BAG_L = 25
BOARD_M = 2.4
OVERHANG = 0.25
FABRIC_W = 2

def sand_plan(boxL, boxW, depthCm):
    if not (boxL > 0) or not (boxW > 0) or not (depthCm > 0):
        return {"error": "the box length, width and fill depth must be positive"}
    liters = round1(boxL * boxW * depthCm * 10)
    bags = math.ceil(liters / BAG_L)
    if liters <= 125: verdict = "a top-up job"
    elif liters <= 1000: verdict = "a weekend build"
    else: verdict = "truckload territory"
    return {"liters": liters, "bags": bags, "verdict": verdict}

def frame_plan(boxL, boxW):
    if not (boxL > 0) or not (boxW > 0):
        return {"error": "the box sides must be positive"}
    perimeter = round1(2 * (boxL + boxW))
    boards = math.ceil(perimeter / BOARD_M)
    if perimeter <= 6: verdict = "a step-in box"
    elif perimeter <= 12: verdict = "a sit-in box"
    else: verdict = "a sandbox kingdom"
    return {"perimeter": perimeter, "boards": boards, "posts": 4, "verdict": verdict}

def cover_plan(boxL, boxW):
    if not (boxL > 0) or not (boxW > 0):
        return {"error": "the box sides must be positive"}
    coverL = round1(boxL + 2 * OVERHANG)
    coverW = round1(boxW + 2 * OVERHANG)
    area = round1(coverL * coverW)
    strips = math.ceil(coverW / FABRIC_W)
    if area <= 4: verdict = "a picnic-rug cover"
    elif area <= 12: verdict = "a real tarp"
    else: verdict = "a small sail"
    return {"coverL": coverL, "coverW": coverW, "area": area, "strips": strips, "verdict": verdict}

def render_sand(r, boxL, boxW, depthCm):
    return ("A box " + fmt(boxL) + " m by " + fmt(boxW) + " m filled " + fmt(depthCm) + " cm deep takes " + fmt(r["liters"])
            + " L of play sand - " + plural(r["bags"], "bag") + " of labeled " + fmt(BAG_L) + " L, " + r["verdict"] + ".")

def render_frame(r, boxL, boxW):
    return ("A frame for a " + fmt(boxL) + " m by " + fmt(boxW) + " m box runs " + fmt(r["perimeter"]) + " m around - "
            + plural(r["boards"], "board") + " of labeled " + fmt(BOARD_M) + " m and " + plural(r["posts"], "corner post")
            + ", " + r["verdict"] + ".")

def render_cover(r, boxL, boxW):
    return ("A cover for a " + fmt(boxL) + " m by " + fmt(boxW) + " m box at a labeled " + fmt(OVERHANG) + " m overhang each side is "
            + fmt(r["coverL"]) + " m by " + fmt(r["coverW"]) + " m - " + fmt(r["area"]) + " m2, " + plural(r["strips"], "strip")
            + " of labeled " + fmt(FABRIC_W) + " m fabric, " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[2,1.5,15],[3,2.4,20],[1,1,5],[2,2,10],[1.2,0.8,10],[4,3,25],[1.5,1.5,8],[0.5,0.5,5],[0,1.5,15],[2,0,15],[2,1.5,0]]:
    add("sandPlan", sand_plan, render_sand, a)
for a in [[2,1.5],[3,2.4],[1,1],[4,3],[0.8,0.8],[2.5,2.5],[5,4],[1.2,0.9],[0,2],[1.5,0]]:
    add("framePlan", frame_plan, render_frame, a)
for a in [[2,1.5],[3,2.4],[1,1],[0.6,0.6],[4,3],[2.5,2],[1.1,0.9],[3.5,3],[0,1],[2,0]]:
    add("coverPlan", cover_plan, render_cover, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
