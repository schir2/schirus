let modal = document.getElementById('modal');
let page_mask = document.getElementById('page-mask');


function openModal() {
    modal.style.display = 'block';
    modal.style.opacity = 1;
    page_mask.style.display = 'block';
}

function closeModal() {
    modal.style.opacity = 0;
    modal.style.display = 'none';
    page_mask.style.display ='none';

}