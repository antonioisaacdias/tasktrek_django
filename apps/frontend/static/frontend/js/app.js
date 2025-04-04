document.querySelectorAll('textarea').forEach(el => {
    el.addEventListener('input', e => {
      e.target.style.height = 'auto';
      e.target.style.height = `${e.target.scrollHeight}px`;
    });
});

const input = document.getElementById('date-input');
const hoje = new Date().toISOString().split('T')[0];
input.value = hoje;