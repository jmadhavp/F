
# Create transfer.html - File transfer interface
transfer_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LocalDrop - File Transfer</title>
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .header {
            background: white;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        .header h1 {
            font-size: 32px;
            color: #1f2937;
            margin-bottom: 8px;
        }
        
        .back-link {
            display: inline-block;
            margin-top: 8px;
            color: #667eea;
            text-decoration: none;
            font-size: 14px;
        }
        
        .transfer-section {
            background: white;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        .drop-zone {
            border: 3px dashed #d1d5db;
            border-radius: 16px;
            padding: 60px 20px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
            background: #f9fafb;
        }
        
        .drop-zone.drag-over {
            border-color: #667eea;
            background: #ede9fe;
        }
        
        .drop-zone-icon {
            font-size: 64px;
            margin-bottom: 16px;
        }
        
        .drop-zone h3 {
            font-size: 24px;
            margin-bottom: 8px;
            color: #1f2937;
        }
        
        .drop-zone p {
            color: #6b7280;
            font-size: 14px;
        }
        
        .file-input {
            display: none;
        }
        
        .btn {
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.2s;
            background: #667eea;
            color: white;
            margin-top: 16px;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        }
        
        .transfer-list {
            margin-top: 32px;
        }
        
        .transfer-item {
            padding: 16px;
            background: #f9fafb;
            border-radius: 12px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        
        .transfer-info {
            flex: 1;
        }
        
        .transfer-name {
            font-weight: 600;
            margin-bottom: 4px;
        }
        
        .transfer-progress {
            width: 100%;
            height: 8px;
            background: #e5e7eb;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 8px;
        }
        
        .transfer-progress-bar {
            height: 100%;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            transition: width 0.3s;
        }
        
        .transfer-status {
            font-size: 14px;
            color: #6b7280;
            margin-top: 4px;
        }
        
        .received-files {
            margin-top: 32px;
        }
        
        .file-card {
            padding: 16px;
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            border-radius: 12px;
            color: white;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        
        .file-icon {
            font-size: 32px;
            margin-right: 16px;
        }
        
        .file-info {
            flex: 1;
        }
        
        .file-name {
            font-weight: 600;
            margin-bottom: 4px;
        }
        
        .file-size {
            font-size: 14px;
            opacity: 0.9;
        }
        
        .download-btn {
            padding: 8px 16px;
            background: rgba(255, 255, 255, 0.2);
            border: 1px solid white;
            border-radius: 8px;
            color: white;
            cursor: pointer;
            font-weight: 500;
        }
        
        .download-btn:hover {
            background: rgba(255, 255, 255, 0.3);
        }
        
        .footer {
            background: white;
            border-radius: 16px;
            padding: 24px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            color: #6b7280;
        }
        
        .footer strong {
            color: #ef4444;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>📁 File Transfer</h1>
        <a href="connect.html" class="back-link">← Back to Connect</a>
    </div>
    
    <div class="transfer-section">
        <h2 style="margin-bottom: 16px;">Send Files</h2>
        
        <div class="drop-zone" id="dropZone" onclick="document.getElementById('fileInput').click()">
            <div class="drop-zone-icon">📤</div>
            <h3>Drop files here</h3>
            <p>or click to select files</p>
            <p style="margin-top: 8px; font-size: 12px; opacity: 0.7;">All file types supported • No size limit</p>
            <button class="btn">📁 Select Files</button>
        </div>
        
        <input type="file" id="fileInput" class="file-input" multiple onchange="handleFiles(this.files)">
        
        <div class="transfer-list" id="transferList" style="display: none;">
            <h3 style="margin-bottom: 16px;">Transfer Progress</h3>
        </div>
    </div>
    
    <div class="transfer-section received-files" id="receivedSection" style="display: none;">
        <h2 style="margin-bottom: 16px;">📥 Received Files</h2>
        <div id="receivedFiles"></div>
    </div>
    
    <div class="footer">
        <p>Made with <strong>❤️</strong> in India by <strong>PROGRAMMER MJ</strong></p>
        <p style="margin-top: 8px; font-size: 14px;">LocalDrop v2.0.0 - Instant File Sharing</p>
    </div>
    
    <script>
        const dropZone = document.getElementById('dropZone');
        const transferList = document.getElementById('transferList');
        const receivedSection = document.getElementById('receivedSection');
        const receivedFiles = document.getElementById('receivedFiles');
        
        // Drag and drop handlers
        dropZone.addEventListener('dragover', (e) => {
            e.preventDefault();
            dropZone.classList.add('drag-over');
        });
        
        dropZone.addEventListener('dragleave', () => {
            dropZone.classList.remove('drag-over');
        });
        
        dropZone.addEventListener('drop', (e) => {
            e.preventDefault();
            dropZone.classList.remove('drag-over');
            handleFiles(e.dataTransfer.files);
        });
        
        // Handle file selection
        function handleFiles(files) {
            if (files.length === 0) return;
            
            transferList.style.display = 'block';
            
            Array.from(files).forEach(file => {
                addTransferItem(file);
                simulateTransfer(file);
            });
        }
        
        // Add transfer item to list
        function addTransferItem(file) {
            const item = document.createElement('div');
            item.className = 'transfer-item';
            item.id = 'transfer-' + Date.now();
            
            item.innerHTML = `
                <div class="transfer-info">
                    <div class="transfer-name">📄 ${file.name}</div>
                    <div class="transfer-status">Preparing... • ${formatFileSize(file.size)}</div>
                    <div class="transfer-progress">
                        <div class="transfer-progress-bar" style="width: 0%"></div>
                    </div>
                </div>
            `;
            
            transferList.appendChild(item);
        }
        
        // Simulate file transfer
        function simulateTransfer(file) {
            let progress = 0;
            const itemId = 'transfer-' + (Date.now() - 1);
            const item = document.getElementById(itemId);
            if (!item) return;
            
            const progressBar = item.querySelector('.transfer-progress-bar');
            const status = item.querySelector('.transfer-status');
            
            const interval = setInterval(() => {
                progress += Math.random() * 15 + 5;
                if (progress >= 100) {
                    progress = 100;
                    clearInterval(interval);
                    status.textContent = '✅ Complete • ' + formatFileSize(file.size);
                    addReceivedFile(file);
                } else {
                    status.textContent = `Sending... ${Math.round(progress)}% • ${formatFileSize(file.size)}`;
                }
                progressBar.style.width = progress + '%';
            }, 200);
        }
        
        // Add received file
        function addReceivedFile(file) {
            receivedSection.style.display = 'block';
            
            const fileCard = document.createElement('div');
            fileCard.className = 'file-card';
            
            const fileIcon = getFileIcon(file.name);
            
            fileCard.innerHTML = `
                <div class="file-icon">${fileIcon}</div>
                <div class="file-info">
                    <div class="file-name">${file.name}</div>
                    <div class="file-size">${formatFileSize(file.size)}</div>
                </div>
                <button class="download-btn" onclick="downloadFile('${file.name}')">
                    ⬇️ Download
                </button>
            `;
            
            receivedFiles.insertBefore(fileCard, receivedFiles.firstChild);
        }
        
        // Get file icon based on extension
        function getFileIcon(filename) {
            const ext = filename.split('.').pop().toLowerCase();
            const icons = {
                'jpg': '🖼️', 'jpeg': '🖼️', 'png': '🖼️', 'gif': '🖼️',
                'mp4': '🎬', 'avi': '🎬', 'mov': '🎬',
                'mp3': '🎵', 'wav': '🎵', 'flac': '🎵',
                'pdf': '📕', 'doc': '📄', 'docx': '📄',
                'zip': '📦', 'rar': '📦', '7z': '📦',
                'js': '💻', 'py': '💻', 'html': '💻'
            };
            return icons[ext] || '📎';
        }
        
        // Format file size
        function formatFileSize(bytes) {
            if (bytes === 0) return '0 Bytes';
            const k = 1024;
            const sizes = ['Bytes', 'KB', 'MB', 'GB'];
            const i = Math.floor(Math.log(bytes) / Math.log(k));
            return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
        }
        
        // Download file (simulated)
        function downloadFile(filename) {
            showToast('Downloading ' + filename);
        }
        
        // Show toast
        function showToast(message) {
            const toast = document.createElement('div');
            toast.textContent = message;
            toast.style.cssText = `
                position: fixed;
                bottom: 20px;
                right: 20px;
                background: #1f2937;
                color: white;
                padding: 16px 24px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
                z-index: 10000;
            `;
            document.body.appendChild(toast);
            setTimeout(() => toast.remove(), 3000);
        }
    </script>
</body>
</html>'''

with open('transfer.html', 'w', encoding='utf-8') as f:
    f.write(transfer_html)

print("✅ transfer.html created - File transfer interface")
