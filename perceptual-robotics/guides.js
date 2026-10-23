const figures = document.querySelectorAll('.figure .image-shell');
if (figures.length) {
  const dialog = document.createElement('dialog');
  dialog.className = 'image-dialog';
  dialog.setAttribute('aria-label', 'Full-size Lab screenshot');
  dialog.innerHTML = '<header><span>Lab screenshot</span><span><a target="_blank" rel="noopener">Full size ↗</a><button type="button" aria-label="Close screenshot">Close ×</button></span></header><img alt="">';
  document.body.append(dialog);
  const image = dialog.querySelector('img');
  const fullSize = dialog.querySelector('a');
  dialog.querySelector('button').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', (event) => { if (event.target === dialog) dialog.close(); });
  for (const figure of figures) {
    figure.addEventListener('click', (event) => {
      event.preventDefault();
      image.src = figure.href;
      image.alt = figure.querySelector('img').alt;
      fullSize.href = figure.href;
      dialog.showModal();
    });
  }
}
for (const section of document.querySelectorAll('.guide-section')) {
  const notes = [...section.querySelectorAll('.note')];
  const markers = [...section.querySelectorAll('.marker')];
  function highlight(index, active) {
    notes[index]?.classList.toggle('is-active', active);
    markers[index]?.classList.toggle('is-active', active);
  }
  for (const [index, note] of notes.entries()) {
    note.addEventListener('pointerenter', () => highlight(index, true));
    note.addEventListener('pointerleave', () => highlight(index, false));
  }
  for (const [index, marker] of markers.entries()) {
    marker.addEventListener('pointerenter', () => highlight(index, true));
    marker.addEventListener('pointerleave', () => highlight(index, false));
  }
}
