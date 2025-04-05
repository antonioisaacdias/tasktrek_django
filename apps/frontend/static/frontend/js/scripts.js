document.querySelectorAll('textarea').forEach(el => {
    el.addEventListener('input', e => {
      e.target.style.height = 'auto';
      e.target.style.height = `${e.target.scrollHeight}px`;
    });
});



