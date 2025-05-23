document.querySelectorAll('textarea').forEach(el => {
    el.addEventListener('input', e => {
      e.target.style.height = 'auto';
      e.target.style.height = `${e.target.scrollHeight}px`;
    });
});

function exibirErro(event) {
  try {
      const data = JSON.parse(event.detail.xhr.responseText);
      const msg = Object.values(data)[0];
      const root = document.querySelector('[x-data]');
      root.__x.$data.erro = Array.isArray(msg) ? msg[0] : msg;
      root.__x.$data.sucesso = '';
  } catch (e) {
      console.error('Erro inesperado:', e);
  }
}

function exibirSucesso(event) {
  if (event.detail.xhr.status === 201) {
      const root = document.querySelector('[x-data]');
      root.__x.$data.sucesso = 'Tarefa criada com sucesso!';
      root.__x.$data.erro = '';
  }
}

function completarTarefa(task) { 

    fetch(`/api/tasks/complete/${task.id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('meta[name=csrf-token]').content
        }
    })
    .then(res => res.json())
    .then(data => {
        task.is_completed = data.is_completed  // atualiza visualmente
    })
    .catch(err => console.error('Erro ao completar tarefa', err))
}

