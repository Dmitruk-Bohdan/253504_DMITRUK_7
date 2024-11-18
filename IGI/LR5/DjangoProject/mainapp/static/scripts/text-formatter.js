document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('toggle-settings').addEventListener('change', function() {
        const styleForm = document.getElementById('style-form');
        styleForm.style.display = this.checked ? 'block' : 'none';
    });
    
    document.getElementById('apply-styles').addEventListener('click', function() {
        const fontSize = document.getElementById('font-size').value + 'px';
        const textColor = document.getElementById('text-color').value;
        const backgroundColor = document.getElementById('background-color').value;
    
        const textBlocks = document.querySelectorAll('.text-block');
        
        textBlocks.forEach(block => {
            block.style.fontSize = fontSize;
            block.style.color = textColor;
            block.style.backgroundColor = backgroundColor;
        });
    });
});
