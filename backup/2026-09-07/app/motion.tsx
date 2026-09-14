"use client";

import { useEffect } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

/**
 * Camada de movimento do site.
 *
 * Princípios que este componente respeita:
 * - conteúdo nunca pode ficar invisível. O gatilho da revelação é uma verificação
 *   determinística de posição, e não um evento: um elemento já ultrapassado é
 *   revelado na mesma hora, em vez de ficar preso em opacidade zero.
 * - o CSS continua sendo a fonte do estado final: aqui só mudam opacidade, deslocamento e escala.
 * - `prefers-reduced-motion` desliga tudo e nada chega a ser escondido.
 * - seletores ausentes na página atual são ignorados.
 */
export default function Motion() {
  useEffect(() => {
    /* A montagem espera a hidratação assentar: o GSAP escreve `style` inline e,
       se isso acontecer enquanto o React ainda hidrata a árvore, o React acusa
       divergência entre o HTML do servidor e o do cliente. */
    let mm: ReturnType<typeof gsap.matchMedia> | null = null;

    const setup = () => {
    gsap.registerPlugin(ScrollTrigger);

    mm = gsap.matchMedia();

    mm.add("(prefers-reduced-motion: no-preference)", () => {
      type Entry = { el: HTMLElement; stagger: number };
      const pending = new Map<HTMLElement, Entry>();

      const has = (selector: string) => document.querySelector(selector) !== null;
      const pick = (selector: string) => gsap.utils.toArray<HTMLElement>(selector);

      /** Marca elementos para revelar quando entrarem (ou já estiverem) na área visível. */
      const reveal = (
        selector: string,
        options: { y?: number; x?: number; stagger?: number; scale?: number } = {},
      ) => {
        const items = pick(selector);
        if (!items.length) return;
        gsap.set(items, { opacity: 0, y: options.y ?? 26, x: options.x ?? 0, scale: options.scale ?? 1 });
        items.forEach((el) => pending.set(el, { el, stagger: options.stagger ?? 0.08 }));
      };

      /** Anima um traçado de SVG como se estivesse sendo desenhado. */
      const draw = (paths: NodeListOf<SVGPathElement>, trigger: Element, step = 0) => {
        paths.forEach((path, index) => {
          let length = 0;
          try {
            length = path.getTotalLength();
          } catch {
            return;
          }
          if (!length) return;
          gsap.fromTo(
            path,
            { strokeDasharray: length, strokeDashoffset: length },
            {
              strokeDashoffset: 0,
              duration: 1.3,
              delay: index * step,
              ease: "power2.inOut",
              scrollTrigger: { trigger, start: "top 85%", once: true },
            },
          );
        });
      };

      /* ---------- entrada do topo ---------- */

      const heroCopy = document.querySelector(".hero-copy") ?? document.querySelector(".ita-hero-copy");
      if (heroCopy) {
        const intro = gsap.timeline({ defaults: { ease: "power3.out" } });
        intro.from(".site-header", { y: -22, opacity: 0, duration: 0.55 });
        if (has(".hero-mark")) intro.from(".hero-mark", { opacity: 0, y: 14, duration: 0.55 }, "-=0.28");
        if (has(".ita-wordmark")) intro.from(".ita-wordmark", { opacity: 0, y: 16, duration: 0.55 }, "-=0.3");
        intro
          .from(heroCopy.querySelectorAll("h1"), { opacity: 0, y: 32, duration: 0.85 }, "-=0.25")
          .from(heroCopy.querySelectorAll(".hero-lead"), { opacity: 0, y: 22, duration: 0.65 }, "-=0.5")
          .from(heroCopy.querySelectorAll(".hero-actions > *"), { opacity: 0, y: 16, duration: 0.55, stagger: 0.1 }, "-=0.4");
        if (has(".hero-pillars span")) intro.from(".hero-pillars span", { opacity: 0, y: 12, duration: 0.45, stagger: 0.08 }, "-=0.35");
        if (has(".logo-frame")) intro.from(".logo-frame", { opacity: 0, scale: 0.9, duration: 1 }, "-=1");
        if (has(".territory-map")) intro.from(".territory-map", { opacity: 0, scale: 0.9, duration: 1 }, "-=1");
        if (has(".territory-status")) intro.from(".territory-status", { opacity: 0, x: 24, duration: 0.6 }, "-=0.4");
        if (has(".map-node")) intro.from(".map-node", { opacity: 0, scale: 0, duration: 0.45, stagger: 0.14, ease: "back.out(2)" }, "-=0.3");
      }

      /* malha de fundo em parallax */
      const heroSection = document.querySelector(".hero") ?? document.querySelector(".ita-hero");
      const heroGrid = document.querySelector(".hero-grid") ?? document.querySelector(".ita-grid");
      if (heroSection && heroGrid) {
        gsap.to(heroGrid, {
          yPercent: 14,
          ease: "none",
          scrollTrigger: { trigger: heroSection, start: "top top", end: "bottom top", scrub: true },
        });
      }

      /* ---------- títulos, textos, cards ---------- */

      reveal(".section-heading > div, .section-heading > p", { y: 28, stagger: 0.1 });
      reveal(".engineering-copy > *, .about-copy > *, .contact-layout > div > *", { y: 24 });
      reveal(".process-intro > *", { y: 24 });
      reveal(".ita-lead", { y: 20 });
      reveal(".product-feature-copy > *", { y: 24, stagger: 0.1 });

      reveal(".area-card", { y: 30, stagger: 0.1 });
      reveal(".experience-card", { y: 32, stagger: 0.11 });
      reveal(".solution-card", { y: 28, stagger: 0.07 });
      reveal(".client-card", { y: 24, stagger: 0.1 });
      reveal(".ita-investigation-card", { y: 28, stagger: 0.1 });
      reveal(".audience-grid div", { y: 20, stagger: 0.06 });
      reveal(".ita-flow li", { y: 26, stagger: 0.11 });
      reveal(".process-list li", { x: -22, y: 0, stagger: 0.08 });
      reveal(".principles-list li", { x: -20, y: 0, stagger: 0.08 });
      reveal(".technology-line, .scope-note", { y: 18 });
      reveal(".founder-card", { y: 22 });

      /* ---------- grafo de Soluções sob medida ---------- */

      const graph = document.querySelector<HTMLElement>(".capability-graph");
      if (graph) {
        draw(graph.querySelectorAll<SVGPathElement>(".graph-connections path"), graph);
        reveal(".capability-hub", { y: 0, scale: 0.75 });
        reveal(".capability-node", { y: 0, scale: 0.9, stagger: 0.09 });
      }

      /* ---------- símbolo da VPC-ITA ---------- */

      const itaSymbol = document.querySelector<HTMLElement>(".ita-symbol");
      const itaSvg = itaSymbol?.querySelector("svg");
      if (itaSymbol && itaSvg) draw(itaSvg.querySelectorAll<SVGPathElement>("path"), itaSymbol, 0.16);

      /* ---------- marca da seção Sobre, em parallax ---------- */

      const aboutSection = document.querySelector(".section-about");
      const aboutMark = document.querySelector(".about-mark img");
      if (aboutSection && aboutMark) {
        gsap.to(aboutMark, {
          yPercent: -10,
          ease: "none",
          scrollTrigger: { trigger: aboutSection, start: "top bottom", end: "bottom top", scrub: true },
        });
      }

      /* ---------- gatilho da revelação ----------
         Verificação de posição, e não um evento de entrada: qualquer elemento que
         já esteja no limiar — ou acima dele, porque a página foi rolada — é revelado.
         O disparo é síncrono no scroll (sem requestAnimationFrame, que pode ser
         suspenso quando a aba não está pintando) e tem um intervalo de reforço. */
      let last = 0;
      const flush = (force = false) => {
        if (!pending.size) return;
        const now = performance.now();
        if (!force && now - last < 60) return;
        last = now;
        const limit = window.innerHeight * 0.92;
        const due: Entry[] = [];
        for (const entry of pending.values()) {
          if (entry.el.getBoundingClientRect().top < limit) due.push(entry);
        }
        if (!due.length) return;
        due.forEach((entry) => pending.delete(entry.el));
        due.sort((a, b) => a.el.getBoundingClientRect().top - b.el.getBoundingClientRect().top);
        gsap.to(
          due.map((entry) => entry.el),
          {
            opacity: 1,
            y: 0,
            x: 0,
            scale: 1,
            duration: 0.7,
            ease: "power3.out",
            stagger: Math.min(due[0].stagger, 1.2 / due.length),
            overwrite: true,
          },
        );
      };
      const schedule = () => flush();

      window.addEventListener("scroll", schedule, { passive: true });
      window.addEventListener("resize", schedule, { passive: true });
      const onLoad = () => {
        ScrollTrigger.refresh();
        flush(true);
      };
      if (document.readyState === "complete") onLoad();
      else window.addEventListener("load", onLoad, { once: true });
      flush(true);

      /* reforço: cobre rolagem programática e layout que assenta depois das fontes */
      const beat = window.setInterval(() => {
        if (!pending.size) window.clearInterval(beat);
        else flush(true);
      }, 350);

      /* rede de segurança final: nada pode permanecer invisível por falha de gatilho */
      const guard = window.setTimeout(() => {
        if (!pending.size) return;
        const rest = [...pending.keys()].filter((el) => el.getBoundingClientRect().top < window.innerHeight);
        if (!rest.length) return;
        rest.forEach((el) => pending.delete(el));
        gsap.to(rest, { opacity: 1, y: 0, x: 0, scale: 1, duration: 0.4, overwrite: true });
      }, 3000);

      return () => {
        window.clearTimeout(guard);
        window.clearInterval(beat);
        window.removeEventListener("scroll", schedule);
        window.removeEventListener("resize", schedule);
        window.removeEventListener("load", onLoad);
      };
    });

    };

    let start: number | undefined;
    const kick = () => {
      start = window.setTimeout(setup, 0);
    };
    if (document.readyState === "complete") kick();
    else window.addEventListener("load", kick, { once: true });

    return () => {
      window.clearTimeout(start);
      window.removeEventListener("load", kick);
      mm?.revert();
    };
  }, []);

  return null;
}
