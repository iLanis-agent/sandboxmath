(function (root) {
  "use strict";
  var BAG_L = 25;      // labeled play-sand bag, liters
  var BOARD_M = 2.4;   // labeled frame board length, m
  var OVERHANG = 0.25; // labeled cover overhang each side, m
  var FABRIC_W = 2;    // labeled cover fabric width, m

  function round1(x) { return Math.round(x * 10) / 10; }
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }

  function sandPlan(boxL, boxW, depthCm) {
    if (!(boxL > 0) || !(boxW > 0) || !(depthCm > 0)) return { error: "the box length, width and fill depth must be positive" };
    var liters = round1(boxL * boxW * depthCm * 10);
    var bags = Math.ceil(liters / BAG_L);
    var verdict;
    if (liters <= 125) verdict = "a top-up job";
    else if (liters <= 1000) verdict = "a weekend build";
    else verdict = "truckload territory";
    return { liters: liters, bags: bags, verdict: verdict };
  }

  function framePlan(boxL, boxW) {
    if (!(boxL > 0) || !(boxW > 0)) return { error: "the box sides must be positive" };
    var perimeter = round1(2 * (boxL + boxW));
    var boards = Math.ceil(perimeter / BOARD_M);
    var verdict;
    if (perimeter <= 6) verdict = "a step-in box";
    else if (perimeter <= 12) verdict = "a sit-in box";
    else verdict = "a sandbox kingdom";
    return { perimeter: perimeter, boards: boards, posts: 4, verdict: verdict };
  }

  function coverPlan(boxL, boxW) {
    if (!(boxL > 0) || !(boxW > 0)) return { error: "the box sides must be positive" };
    var coverL = round1(boxL + 2 * OVERHANG);
    var coverW = round1(boxW + 2 * OVERHANG);
    var area = round1(coverL * coverW);
    var strips = Math.ceil(coverW / FABRIC_W);
    var verdict;
    if (area <= 4) verdict = "a picnic-rug cover";
    else if (area <= 12) verdict = "a real tarp";
    else verdict = "a small sail";
    return { coverL: coverL, coverW: coverW, area: area, strips: strips, verdict: verdict };
  }

  function renderSand(r, boxL, boxW, depthCm) {
    return "A box " + boxL + " m by " + boxW + " m filled " + depthCm + " cm deep takes " + r.liters
      + " L of play sand - " + plural(r.bags, "bag") + " of labeled " + BAG_L + " L, " + r.verdict + ".";
  }

  function renderFrame(r, boxL, boxW) {
    return "A frame for a " + boxL + " m by " + boxW + " m box runs " + r.perimeter + " m around - "
      + plural(r.boards, "board") + " of labeled " + BOARD_M + " m and " + plural(r.posts, "corner post") + ", " + r.verdict + ".";
  }

  function renderCover(r, boxL, boxW) {
    return "A cover for a " + boxL + " m by " + boxW + " m box at a labeled " + OVERHANG + " m overhang each side is "
      + r.coverL + " m by " + r.coverW + " m - " + r.area + " m2, " + plural(r.strips, "strip")
      + " of labeled " + FABRIC_W + " m fabric, " + r.verdict + ".";
  }

  var api = { sandPlan: sandPlan, framePlan: framePlan, coverPlan: coverPlan, renderSand: renderSand, renderFrame: renderFrame, renderCover: renderCover };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.SandboxMath = api;
})(this);
