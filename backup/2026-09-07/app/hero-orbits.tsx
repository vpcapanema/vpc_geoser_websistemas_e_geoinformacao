"use client";

import { useEffect, useRef } from "react";

const TAU = Math.PI * 2;
const CAMERA = 900;
const SEGMENTS = 512;
const AXIS_ROTATION = 8;
// Static, deterministic scenery: no extra animation loop or image downloads.
const stars = Array.from({ length: 96 }, (_, i) => ({
  x: 18 + ((i * 173 + i * i * 13) % 684),
  y: 12 + ((i * 97 + i * i * 7) % 456),
  radius: i % 13 === 0 ? 1.65 : i % 4 === 0 ? 1 : 0.55,
  opacity: 0.22 + (i % 6) * 0.11,
}));
// Equal, centered ellipses in opposing planes. Positive Z faces the camera.
// A small depth separation keeps the crossings unambiguous.
const orbits = [
  { tilt: 58, rotation: -25, depthOffset: 12, id: "territorio", radius: 350, period: 28, phase: Math.PI / 2, color: [141, 213, 0], label: "Território", width: 104 },
  { tilt: -58, rotation: 25, depthOffset: -12, id: "dados", radius: 350, period: 34, phase: -Math.PI / 2, color: [17, 184, 216], label: "Dados", width: 84 },
];
type Orbit = typeof orbits[number];

function project(orbit: Orbit, angle: number) {
  const tilt = orbit.tilt * Math.PI / 180, rotation = (orbit.rotation + AXIS_ROTATION) * Math.PI / 180;
  const x = orbit.radius * Math.cos(angle), y = orbit.radius * Math.sin(angle) * Math.cos(tilt);
  const z = orbit.radius * Math.sin(angle) * Math.sin(tilt) + orbit.depthOffset, scale = CAMERA / (CAMERA - z);
  // Orthographic paths stay regular and centered; depth still sizes tubes/cards.
  return { x: x * Math.cos(rotation) - y * Math.sin(rotation),
    y: x * Math.sin(rotation) + y * Math.cos(rotation), z, scale };
}
function edge(orbit: Orbit, angle: number, offset: number) {
  const p = project(orbit, angle), next = project(orbit, angle + 0.0001);
  const dx = next.x - p.x, dy = next.y - p.y, length = Math.hypot(dx, dy);
  return `${p.x - dy / length * offset * p.scale},${p.y + dx / length * offset * p.scale}`;
}
function strip(orbit: Orbit, start: number, end: number, low: number, high: number) {
  return new Path2D(`M${edge(orbit, start, low)} L${edge(orbit, end, low)} L${edge(orbit, end, high)} L${edge(orbit, start, high)} Z`);
}
function buildTubes(configs: Orbit[]) {
  // One depth interval for both rings: no independent lighting/width reference.
  const extremes = configs.flatMap((orbit) => [project(orbit, Math.PI / 2).z, project(orbit, -Math.PI / 2).z]);
  const nearest = Math.max(...extremes), farthest = Math.min(...extremes);
  return configs.flatMap((orbit) => Array.from({ length: SEGMENTS }, (_, index) => {
    const start = index * TAU / SEGMENTS, end = (index + 1) * TAU / SEGMENTS;
    const p = project(orbit, (start + end) / 2), a = project(orbit, start), b = project(orbit, end);
    const near = (p.z - farthest) / (nearest - farthest);
    // Shared upper-left light: curved metal has a narrow reflection and a dark rim.
    const dx = b.x - a.x, dy = b.y - a.y, length = Math.hypot(dx, dy);
    const lightFacing = (-dy / length) * -0.6 + (dx / length) * -0.8;
    const side = lightFacing >= 0 ? 1 : -1;
    const reflection = Math.pow(Math.abs(lightFacing), 4) * (0.65 + 0.35 * near);
    const base = orbit.color.map((v) => v * (0.65 + 0.35 * near));
    const rgb = (values: number[]) => `rgb(${values.map(Math.round).join(" ")})`;
    return {
      orbit: orbit.id, depth: p.z,
      left: Math.min(a.x, b.x) - 7, right: Math.max(a.x, b.x) + 7,
      top: Math.min(a.y, b.y) - 7, bottom: Math.max(a.y, b.y) + 7,
      color: rgb(base),
      highlight: rgb(base.map((v) => v + (255 - v) * (0.55 + 0.4 * reflection))),
      glint: rgb(base.map((v) => v + (255 - v) * (0.8 + 0.2 * reflection))),
      shadow: rgb(base.map((v) => v * (0.22 + 0.12 * near))),
      body: strip(orbit, start - 0.001, end + 0.001, -1.45, 1.45),
      light: strip(orbit, start - 0.001, end + 0.001, -side * 0.15, side * 1.05),
      shine: strip(orbit, start - 0.001, end + 0.001, side * 0.2, side * 0.8),
      shade: strip(orbit, start - 0.001, end + 0.001, -side * 0.8, -side * 1.45),
    };
  })).sort((a, b) => a.depth - b.depth);
}
type Tube = ReturnType<typeof buildTubes>[number];
function drawTube(ctx: CanvasRenderingContext2D, tube: Tube) {
  ctx.fillStyle = tube.color; ctx.fill(tube.body);
  // Opaque shading avoids dark seams where adjacent fragments overlap.
  ctx.fillStyle = tube.highlight; ctx.fill(tube.light);
  ctx.fillStyle = tube.glint; ctx.fill(tube.shine);
  ctx.fillStyle = tube.shadow; ctx.fill(tube.shade);
}

/** Labels and icons are rasterized once at sufficient resolution for the near pass. */
function cardSprite(orbit: Orbit) {
  const canvas = document.createElement("canvas");
  canvas.width = (orbit.width + 4) * 4; canvas.height = 46 * 4;
  const ctx = canvas.getContext("2d")!;
  ctx.scale(4, 4);
  ctx.fillStyle = "rgba(3,16,43,0.5)";
  ctx.beginPath(); ctx.roundRect(2, 4, orbit.width, 40, 5); ctx.fill();
  ctx.fillStyle = "#0b2349"; ctx.strokeStyle = "#45617d"; ctx.lineWidth = 0.8;
  ctx.beginPath(); ctx.roundRect(0.5, 0.5, orbit.width - 1, 39, 5); ctx.fill(); ctx.stroke();
  ctx.strokeStyle = "rgba(139,167,192,0.4)";
  ctx.beginPath(); ctx.moveTo(6, 2); ctx.lineTo(orbit.width - 6, 2); ctx.stroke();
  ctx.fillStyle = "#e8f1fb"; ctx.font = "700 12px Arial"; ctx.fillText(orbit.label, 32, 24);
  ctx.translate(11, 13); ctx.scale(14 / 24, 14 / 24);
  ctx.strokeStyle = "#8dd500"; ctx.lineWidth = 1.8; ctx.lineCap = "round"; ctx.lineJoin = "round";
  // Paths from the installed Lucide Radar/Database icons (ISC license).
  if (orbit.id === "dados") {
    ctx.beginPath(); ctx.ellipse(12, 5, 9, 3, 0, 0, TAU); ctx.stroke();
    ctx.stroke(new Path2D("M3 5V19A9 3 0 0 0 21 19V5 M3 12A9 3 0 0 0 21 12"));
  } else {
    ctx.stroke(new Path2D("M19.07 4.93A10 10 0 0 0 6.99 3.34 M4 6h.01 M2.29 9.62A10 10 0 1 0 21.31 8.35 M16.24 7.76A6 6 0 1 0 8.23 16.67 M12 18h.01 M17.99 11.66A6 6 0 0 1 15.77 16.67 M13.41 10.59l5.66-5.66"));
    ctx.beginPath(); ctx.arc(12, 12, 2, 0, TAU); ctx.stroke();
  }
  return canvas;
}

export default function HeroOrbits() {
  const backRef = useRef<HTMLCanvasElement>(null), frontRef = useRef<HTMLCanvasElement>(null);
  useEffect(() => {
    const back = backRef.current, front = frontRef.current;
    if (!back || !front) return;
    const backContext = back.getContext("2d"), frontContext = front.getContext("2d");
    if (!backContext || !frontContext) return;
    const layers = [back, front].map((canvas, index) => ({ canvas,
      ctx: index === 0 ? backContext : frontContext, cache: document.createElement("canvas"), tubes: [] as Tube[] }));
    const sprites = orbits.map(cardSprite), reduced = window.matchMedia("(prefers-reduced-motion: reduce)");
    const configs = orbits;
    let cardSize = 1, pixelScale = 1, offsetX = 0, offsetY = 0;
    let frame = 0, previous = 0, seconds = 0, visible = true;
    const worldTransform = (ctx: CanvasRenderingContext2D) => ctx.setTransform(pixelScale, 0, 0, pixelScale, offsetX, offsetY);
    const draw = () => {
      const cards = configs.map((orbit, index) => {
        const p = project(orbit, orbit.phase + seconds / orbit.period * TAU), scale = p.scale * cardSize;
        return { orbit, sprite: sprites[index], ...p, scale,
          left: p.x - orbit.width / 2 * scale, top: p.y - 20 * scale,
          right: p.x + (orbit.width / 2 + 4) * scale, bottom: p.y + 26 * scale };
      }).sort((a, b) => a.z - b.z);
      layers.forEach((layer, index) => {
        const ctx = layer.ctx;
        ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.clearRect(0, 0, layer.canvas.width, layer.canvas.height);
        ctx.drawImage(layer.cache, 0, 0); worldTransform(ctx);
        for (const card of cards) {
          if ((card.z >= 0 ? 1 : 0) !== index) continue;
          ctx.drawImage(card.sprite, card.left, card.top, card.right - card.left, card.bottom - card.top);
          // Only nearer fragments overlapping the card need repainting.
          ctx.save(); ctx.beginPath();
          ctx.rect(card.left, card.top, card.right - card.left, card.bottom - card.top); ctx.clip();
          for (const tube of layer.tubes) {
            if (tube.orbit === card.orbit.id || tube.depth <= card.z || tube.right < card.left ||
              tube.left > card.right || tube.bottom < card.top || tube.top > card.bottom) continue;
            drawTube(ctx, tube);
          }
          ctx.restore();
        }
      });
    };
    const resize = () => {
      const bounds = back.getBoundingClientRect();
      if (!bounds.width || !bounds.height) return;
      // The canvas has an 80px gutter for rails/cards outside the former SVG viewBox.
      const scale = Math.min((bounds.width - 160) / 720, (bounds.height - 160) / 420), ratio = Math.min(window.devicePixelRatio || 1, 2);
      cardSize = Math.min(1.65, Math.max(1, 0.88 / scale));
      const globe = back.parentElement?.querySelector<HTMLElement>(".logo-frame");
      pixelScale = scale * ratio;
      offsetX = (globe ? globe.offsetLeft + globe.offsetWidth / 2 - back.offsetLeft : bounds.width / 2) * ratio;
      offsetY = (globe ? globe.offsetTop + globe.offsetHeight / 2 - back.offsetTop : bounds.height / 2) * ratio;
      const tubes = buildTubes(configs);
      layers.forEach((layer, index) => {
        layer.canvas.width = layer.cache.width = Math.ceil(bounds.width * ratio);
        layer.canvas.height = layer.cache.height = Math.ceil(bounds.height * ratio);
        layer.tubes = tubes.filter((tube) => (tube.depth >= 0 ? 1 : 0) === index);
        const cached = layer.cache.getContext("2d")!; worldTransform(cached);
        layer.tubes.forEach((tube) => drawTube(cached, tube));
      });
      draw();
    };
    const tick = (now: number) => {
      if (previous) seconds += (now - previous) / 1000;
      previous = now; draw(); frame = requestAnimationFrame(tick);
    };
    const sync = () => {
      cancelAnimationFrame(frame); previous = 0;
      if (!reduced.matches && !document.hidden && visible) frame = requestAnimationFrame(tick);
    };
    resize();
    const observer = new ResizeObserver(resize); observer.observe(back);
    const intersection = new IntersectionObserver(([entry]) => { visible = entry.isIntersecting; sync(); }); intersection.observe(back);
    reduced.addEventListener("change", sync); document.addEventListener("visibilitychange", sync); sync();
    return () => {
      cancelAnimationFrame(frame); observer.disconnect(); intersection.disconnect();
      reduced.removeEventListener("change", sync); document.removeEventListener("visibilitychange", sync);
    };
  }, []);
  return <>
    <span className="sr-only">Território e Dados em órbitas ao redor do globo.</span>
    <svg className="hero-space" viewBox="0 0 720 480" aria-hidden="true" focusable="false">
      <defs>
        <radialGradient id="hero-nebula">
          <stop stopColor="#2584ba" stopOpacity=".13" />
          <stop offset=".5" stopColor="#2551a3" stopOpacity=".05" />
          <stop offset="1" stopColor="#2551a3" stopOpacity="0" />
        </radialGradient>
        <radialGradient id="hero-planet" cx="28%" cy="24%" r="76%">
          <stop stopColor="#a7c9db" /><stop offset=".36" stopColor="#446788" />
          <stop offset=".75" stopColor="#142c4e" /><stop offset="1" stopColor="#07162f" />
        </radialGradient>
        <radialGradient id="hero-star-glow">
          <stop stopColor="#e4f4ff" stopOpacity=".8" />
          <stop offset=".12" stopColor="#c2e6ff" stopOpacity=".4" />
          <stop offset=".4" stopColor="#84cfff" stopOpacity=".1" />
          <stop offset="1" stopColor="#84cfff" stopOpacity="0" />
        </radialGradient>
      </defs>
      <ellipse cx="420" cy="230" rx="320" ry="140" transform="rotate(-32 420 230)" fill="url(#hero-nebula)" />
      <ellipse cx="280" cy="270" rx="240" ry="65" transform="rotate(-32 280 270)" fill="url(#hero-nebula)" opacity=".5" />
      <g fill="#d5e9f6">
        {stars.map((star, i) => <circle key={i} cx={star.x} cy={star.y} r={star.radius} opacity={star.opacity} />)}
      </g>
      <g fill="url(#hero-star-glow)">
        <circle cx="104" cy="111" r="8" /><circle cx="604" cy="337" r="7" />
        <circle cx="521" cy="56" r="6" />
      </g>
      <g fill="#e4f4ff" opacity=".85">
        <circle cx="104" cy="111" r="1.1" /><circle cx="604" cy="337" r=".9" />
        <circle cx="521" cy="56" r=".8" />
      </g>
      <circle cx="617" cy="98" r="12" fill="url(#hero-planet)" opacity=".75" />
      <circle cx="112" cy="367" r="6" fill="url(#hero-planet)" opacity=".6" />
    </svg>
    <canvas ref={backRef} className="orbit-scene orbit-scene-back" aria-hidden="true" />
    <canvas ref={frontRef} className="orbit-scene orbit-scene-front" aria-hidden="true" />
  </>;
}
