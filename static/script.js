form.addEventListener('submit', function(event) {
    event.preventDefault();
    const fileInput = document.querySelector('input[type="file"]');
    if (!fileInput || !fileInput.files[0]) {
        alert('Please select a file to upload.');
        return;
    }
    const file = fileInput.files[0];
    const allowedTypes = ['image/png', 'image/jpeg', 'application/pdf'];
    if (!allowedTypes.includes(file.type)) {
        alert('Invalid file type. Please upload a PNG, JPEG, or PDF file.');
        return;
    }
    if (file.size > 5 * 1024 * 1024) { // 5 MB limit
        alert('File size exceeds the 5 MB limit.');
        return;
    }
    alert('File Uploaded! Scanning...');
});