// Typing multiple elements based on data-text attributes
document.addEventListener('DOMContentLoaded', () => {
  const typers = Array.from(document.querySelectorAll('[data-text]')).map(el => {
    return {
      el,
      text: el.getAttribute('data-text') || '',
      speed: parseInt(el.getAttribute('data-speed')) || 30,
      index: 0
    };
  });

  function tick() {
    let anyRunning = false;
    typers.forEach(t => {
      if (t.index >= t.text.length) return;
      anyRunning = true;
      const char = t.text.charAt(t.index);

      if (char === '\r') {
        t.index++;
      } else if (char === '\n') {
        if (t.text.charAt(t.index + 1) === '\n') {
          t.el.innerHTML += '<br><br>';
          t.index += 2;
        } else {
          t.el.innerHTML += '<br>';
          t.index++;
        }
      } else {
        const safeChar = char === '<' ? '&lt;' : (char === '>' ? '&gt;' : char);
        t.el.innerHTML += safeChar;
        t.index++;
      }
    });

    if (anyRunning) {
      // choisir un timeout moyen (ici 30ms) pour faire avancer tous les typers.
      setTimeout(tick, 30);
    }
  }

  // démarrer l'animation (si au moins un element existe)
  if (typers.length) tick();
});
