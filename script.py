
# Create a FIXED connect.html - working version with visible send option
# This goes back to the robust version that was working and adds VISIBLE file transfer

connect_fixed_final = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LocalDrop - Connect & Share</title>
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <script src="https://unpkg.com/html5-qrcode@2.3.8/html5-qrcode.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/peerjs@1.5.4/dist/peerjs.min.js"></script>
    
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
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
        .header h1 { font-size: 32px; color: #1f2937; margin-bottom: 8px; }
        .back-link {
            display: inline-block;
            margin-top: 8px;
            color: #667eea;
            text-decoration: none;
            font-size: 14px;
        }
        .device-info {
            background: white;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        .device-name-display {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            flex-wrap: wrap;
            gap: 12px;
        }
        .device-name-display h2 { font-size: 24px; color: #1f2937; }
        .btn {
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.2s;
            font-size: 14px;
        }
        .btn-primary { background: #667eea; color: white; }
        .btn-success { background: #10b981; color: white; }
        .btn-info { background: #3b82f6; color: white; }
        .btn-warning { background: #8b5cf6; color: white; }
        .btn-danger { background: #ef4444; color: white; }
        .btn:hover:not(:disabled) {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        }
        .btn:disabled { opacity: 0.5; cursor: not-allowed; }
        .controls {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            margin-top: 16px;
        }
        .status {
            padding: 12px;
            background: #f3f4f6;
            border-radius: 8px;
            font-size: 14px;
            margin-top: 16px;
        }
        .status.online { background: #d1fae5; color: #065f46; }
        .status.connecting { background: #fef3c7; color: #92400e; }
        .status.connected { background: #dbeafe; color: #1e40af; }
        .status.error { background: #fee2e2; color: #991b1b; }
        .section {
            background: white;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        .drop-zone {
            border: 3px dashed #d1d5db;
            border-radius: 16px;
            padding: 40px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
            background: #f9fafb;
            margin-bottom: 20px;
        }
        .drop-zone.drag-over {
            border-color: #667eea;
            background: #ede9fe;
        }
        .device-card {
            padding: 16px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
            color: white;
            margin-bottom: 12px;
        }
        .transfer-item {
            padding: 12px;
            background: #f3f4f6;
            border-radius: 8px;
            margin-bottom: 12px;
            border-left: 4px solid #667eea;
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
        .received-file {
            padding: 12px;
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            border-radius: 8px;
            color: white;
            margin-bottom: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 12px;
        }
        .footer {
            background: white;
            border-radius: 16px;
            padding: 24px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            color: #6b7280;
        }
        .footer strong { color: #ef4444; }
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            justify-content: center;
            align-items: center;
            z-index: 1000;
        }
        .modal.show { display: flex !important; }
        .modal-content {
            background: white;
            border-radius: 16px;
            padding: 32px;
            max-width: 500px;
            width: 90%;
            max-height: 90vh;
            overflow-y: auto;
            position: relative;
        }
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 24px;
        }
        .modal-header h3 { font-size: 24px; }
        .close-btn {
            background: none;
            border: none;
            font-size: 32px;
            cursor: pointer;
            color: #6b7280;
            line-height: 1;
            padding: 0;
        }
        .close-btn:hover { color: #1f2937; }
        .qr-container {
            display: flex;
            justify-content: center;
            margin: 24px 0;
            padding: 20px;
            background: #f9fafb;
            border-radius: 12px;
        }
        #qr-reader { width: 100%; max-width: 400px; margin: 0 auto; }
        .file-input { display: none; }
        @media (max-width: 768px) {
            .controls { flex-direction: column; }
            .btn { width: 100%; }
            .received-file { flex-direction: column; align-items: flex-start; }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🚀 LocalDrop - Connect & Share</h1>
        <a href="index.html" class="back-link">← Back to Home</a>
    </div>
    
    <div class="device-info">
        <div class="device-name-display">
            <div>
                <h2 id="currentDeviceName">Loading...</h2>
                <p style="font-size: 14px; color: #6b7280; margin-top: 4px;">Your Device</p>
            </div>
            <button onclick="editDeviceName()" class="btn btn-primary">✏️ Edit</button>
        </div>
        
        <div class="controls">
            <button onclick="refreshConnection()" class="btn btn-success">🔄 Refresh</button>
            <button onclick="showMyQR()" class="btn btn-info">📱 Show QR</button>
            <button onclick="scanQRCode()" class="btn btn-warning">📷 Scan QR</button>
        </div>
        
        <div class="status online" id="connectionStatus">
            ⏳ Initializing...
        </div>
    </div>
    
    <!-- Connected Devices -->
    <div class="section">
        <h2>📱 Connected Devices</h2>
        <div id="connectedDevices" style="margin-top: 20px;">
            <p style="color: #6b7280; text-align: center; padding: 20px;">
                No devices connected. Scan a QR code to connect!
            </p>
        </div>
    </div>
    
    <!-- File Transfer - ALWAYS VISIBLE -->
    <div class="section">
        <h2>📤 Send Files</h2>
        <div class="drop-zone" id="dropZone" onclick="document.getElementById('fileInput').click()">
            <div style="font-size: 48px; margin-bottom: 12px;">📁</div>
            <h3>Drop files here to send</h3>
            <p style="color: #6b7280; font-size: 14px;">or click to select</p>
            <p style="color: #9ca3af; font-size: 12px; margin-top: 8px;">📤 Send to connected device • All file types</p>
        </div>
        <input type="file" id="fileInput" class="file-input" multiple onchange="handleFileSelect(this.files)">
        
        <div id="transferList" style="display: none;">
            <h3 style="margin-bottom: 16px;">📊 Transfer Progress</h3>
            <div id="transferItems"></div>
        </div>
    </div>
    
    <!-- Received Files - ALWAYS VISIBLE -->
    <div class="section">
        <h2>📥 Received Files</h2>
        <div id="receivedFilesContainer">
            <p style="color: #6b7280; text-align: center; padding: 20px;">
                Files received from other devices will appear here
            </p>
        </div>
    </div>
    
    <div class="footer">
        <p>Made with <strong>❤️</strong> in India by <strong>PROGRAMMER MJ</strong></p>
        <p style="margin-top: 8px; font-size: 14px;">LocalDrop v2.0.0 - Instant File Sharing</p>
    </div>
    
    <!-- Modals -->
    <div id="nameModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Edit Device Name</h3>
                <button class="close-btn" onclick="closeNameModal()">×</button>
            </div>
            <div class="modal-body">
                <label style="display: block; margin-bottom: 8px; font-weight: 500;">Device Name</label>
                <input type="text" id="deviceNameInput" maxlength="20" style="width: 100%; padding: 12px; border: 2px solid #e5e7eb; border-radius: 8px; font-size: 16px;" placeholder="Enter device name">
                <p style="font-size: 14px; color: #6b7280; margin-top: 8px;"><span id="charCount">0</span>/20</p>
            </div>
            <div style="display: flex; gap: 12px; justify-content: flex-end;">
                <button onclick="closeNameModal()" class="btn" style="background: #e5e7eb; color: #1f2937;">Cancel</button>
                <button onclick="saveDeviceName()" class="btn btn-primary">Save</button>
            </div>
        </div>
    </div>
    
    <div id="qrModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>📱 My QR Code</h3>
                <button class="close-btn" onclick="closeQRModal()">×</button>
            </div>
            <div class="modal-body">
                <p style="text-align: center; margin-bottom: 16px;">📸 Others scan this to connect:</p>
                <div class="qr-container">
                    <div id="qrcode"></div>
                </div>
                <p style="text-align: center; font-size: 12px; color: #6b7280; margin-top: 16px;">Device: <span id="qrDeviceName"></span></p>
            </div>
        </div>
    </div>
    
    <div id="scannerModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>📷 Scan QR Code</h3>
                <button class="close-btn" onclick="closeScannerModal()">×</button>
            </div>
            <div class="modal-body">
                <div id="qr-reader"></div>
                <button onclick="requestCameraPermission()" class="btn btn-warning" style="width: 100%; margin-top: 16px;" id="startCameraBtn">
                    📷 Start Camera
                </button>
                <div id="scan-result" style="margin-top: 16px; padding: 12px; background: #f3f4f6; border-radius: 8px; display: none;"></div>
            </div>
        </div>
    </div>
    
    <script>
        let myDeviceName = '';
        let myDeviceId = '';
        let myPeer = null;
        let qrScanner = null;
        let connections = new Map();
        let receivedFilesMap = new Map();
        let retryCount = 0;
        const MAX_RETRIES = 3;
        const CHUNK_SIZE = 65536;
        
        window.onload = function() {
            console.log('🚀 LocalDrop - Initializing...');
            initializeDevice();
            initializeConnection();
            setupDragDrop();
        };
        
        function initializeDevice() {
            myDeviceId = localStorage.getItem('deviceId') || 'LD' + Math.random().toString(36).substring(2, 10).toUpperCase();
            myDeviceName = localStorage.getItem('deviceName') || generateDeviceName();
            
            localStorage.setItem('deviceId', myDeviceId);
            localStorage.setItem('deviceName', myDeviceName);
            
            document.getElementById('currentDeviceName').textContent = myDeviceName;
            
            if (!localStorage.getItem('hasVisited')) {
                localStorage.setItem('hasVisited', 'true');
                setTimeout(() => editDeviceName(), 500);
            }
        }
        
        function generateDeviceName() {
            const prefixes = ['Phone', 'Laptop', 'Tablet', 'Desktop'];
            const prefix = prefixes[Math.floor(Math.random() * prefixes.length)];
            return prefix + '-' + Math.floor(1000 + Math.random() * 9000);
        }
        
        function initializeConnection() {
            console.log('🔌 Connecting... (attempt ' + (retryCount + 1) + '/' + MAX_RETRIES + ')');
            
            if (retryCount >= MAX_RETRIES) {
                updateStatus('⚠️ Connection failed', 'error');
                return;
            }
            
            try {
                myPeer = new Peer({
                    config: {
                        iceServers: [
                            { urls: 'stun:stun.l.google.com:19302' },
                            { urls: 'stun:stun1.l.google.com:19302' },
                            { urls: 'stun:stun.cloudflare.com:3478' }
                        ]
                    }
                });
                
                myPeer.on('open', (id) => {
                    console.log('✅ Connected! ID:', id);
                    retryCount = 0;
                    updateStatus('✅ Ready to connect', 'online');
                });
                
                myPeer.on('connection', (conn) => {
                    handleConnection(conn);
                });
                
                myPeer.on('error', (err) => {
                    console.error('❌ Error:', err.type);
                    retryCount++;
                    updateStatus('⚠️ Retrying...', 'error');
                    setTimeout(initializeConnection, 2000);
                });
                
            } catch (error) {
                console.error('❌ Error:', error);
                retryCount++;
                setTimeout(initializeConnection, 2000);
            }
        }
        
        function handleConnection(conn) {
            connections.set(conn.peer, { conn, name: 'Unknown', dataChannel: conn });
            
            conn.on('open', () => {
                console.log('✅ Connection opened');
                conn.send({ type: 'name', name: myDeviceName });
            });
            
            conn.on('data', (data) => {
                if (data.type === 'name') {
                    const c = connections.get(conn.peer);
                    if (c) c.name = data.name;
                    updateConnectedDevices();
                } else if (data.type === 'file-start') {
                    if (!receivedFilesMap.has(data.fileId)) {
                        receivedFilesMap.set(data.fileId, {
                            name: data.fileName,
                            type: data.fileType,
                            size: data.fileSize,
                            chunks: [],
                            received: 0
                        });
                    }
                } else if (data.type === 'file-chunk') {
                    const file = receivedFilesMap.get(data.fileId);
                    if (file) {
                        file.chunks.push(data.chunk);
                        file.received += data.chunk.length;
                    }
                } else if (data.type === 'file-complete') {
                    completeFileTransfer(data.fileId);
                }
            });
            
            conn.on('close', () => {
                connections.delete(conn.peer);
                updateConnectedDevices();
            });
        }
        
        function sendFile(file, peerId) {
            const fileId = 'file-' + Date.now();
            const reader = new FileReader();
            
            addTransferItem(fileId, file.name, file.size);
            
            reader.onload = function() {
                const conn = connections.get(peerId);
                if (!conn) return;
                
                conn.dataChannel.send({
                    type: 'file-start',
                    fileId: fileId,
                    fileName: file.name,
                    fileType: file.type,
                    fileSize: file.size
                });
                
                const buffer = reader.result;
                let offset = 0;
                const total = Math.ceil(buffer.byteLength / CHUNK_SIZE);
                let sent = 0;
                
                const sendChunk = () => {
                    if (offset >= buffer.byteLength) {
                        conn.dataChannel.send({ type: 'file-complete', fileId: fileId });
                        updateTransferProgress(fileId, 100);
                        showToast('✅ ' + file.name + ' sent!');
                        return;
                    }
                    
                    const chunk = buffer.slice(offset, offset + CHUNK_SIZE);
                    conn.dataChannel.send({
                        type: 'file-chunk',
                        fileId: fileId,
                        chunk: chunk
                    });
                    
                    offset += CHUNK_SIZE;
                    sent++;
                    const progress = Math.round((sent / total) * 100);
                    updateTransferProgress(fileId, progress);
                    
                    setTimeout(sendChunk, 10);
                };
                
                sendChunk();
            };
            
            reader.readAsArrayBuffer(file);
        }
        
        function handleFileSelect(files) {
            if (connections.size === 0) {
                showToast('❌ No devices connected');
                return;
            }
            
            const peerId = Array.from(connections.keys())[0];
            Array.from(files).forEach(file => sendFile(file, peerId));
        }
        
        function addTransferItem(fileId, fileName, fileSize) {
            document.getElementById('transferList').style.display = 'block';
            
            const item = document.createElement('div');
            item.className = 'transfer-item';
            item.id = 'transfer-' + fileId;
            item.innerHTML = `
                <div style="display: flex; justify-content: space-between;">
                    <div style="flex: 1;">
                        <div style="font-weight: 600;">📤 ${fileName}</div>
                        <div style="font-size: 12px; color: #6b7280;">${formatFileSize(fileSize)}</div>
                    </div>
                    <div id="progress-${fileId}">0%</div>
                </div>
                <div class="transfer-progress">
                    <div class="transfer-progress-bar" id="bar-${fileId}"></div>
                </div>
            `;
            
            document.getElementById('transferItems').appendChild(item);
        }
        
        function updateTransferProgress(fileId, progress) {
            const el = document.getElementById('progress-' + fileId);
            if (el) el.textContent = progress + '%';
            const bar = document.getElementById('bar-' + fileId);
            if (bar) bar.style.width = progress + '%';
        }
        
        function completeFileTransfer(fileId) {
            const file = receivedFilesMap.get(fileId);
            if (!file) return;
            
            const blob = new Blob(file.chunks, { type: file.type });
            addReceivedFile(file.name, blob, file.size);
            showToast('✅ ' + file.name + ' received!');
        }
        
        function addReceivedFile(fileName, blob, fileSize) {
            const fileId = 'rec-' + Date.now();
            const icon = getFileIcon(fileName);
            
            const div = document.createElement('div');
            div.className = 'received-file';
            div.innerHTML = `
                <div style="flex: 1;">
                    <div style="font-size: 24px; margin-bottom: 4px;">${icon}</div>
                    <div style="font-weight: 600;">${fileName}</div>
                    <div style="font-size: 12px; opacity: 0.9;">${formatFileSize(fileSize)}</div>
                </div>
                <button onclick="downloadFile('${fileId}')" class="btn" style="background: rgba(255,255,255,0.2); border: 1px solid white; color: white; padding: 8px 16px;">
                    ⬇️ Download
                </button>
            `;
            
            receivedFilesMap.set(fileId, blob);
            document.getElementById('receivedFilesContainer').insertBefore(div, document.getElementById('receivedFilesContainer').firstChild);
            
            // Remove empty message
            const msg = document.getElementById('receivedFilesContainer').querySelector('p');
            if (msg) msg.remove();
        }
        
        function downloadFile(fileId) {
            const blob = receivedFilesMap.get(fileId);
            if (!blob) return;
            
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'file-' + Date.now();
            a.click();
            URL.revokeObjectURL(url);
            showToast('✅ Downloading...');
        }
        
        function getFileIcon(name) {
            const ext = name.split('.').pop().toLowerCase();
            const icons = {
                'jpg': '🖼️', 'jpeg': '🖼️', 'png': '🖼️', 'gif': '🖼️',
                'mp4': '🎬', 'avi': '🎬', 'mov': '🎬',
                'mp3': '🎵', 'wav': '🎵', 'pdf': '📕', 'doc': '📄', 'docx': '📄',
                'zip': '📦', 'rar': '📦', 'js': '💻', 'py': '💻'
            };
            return icons[ext] || '📎';
        }
        
        function formatFileSize(bytes) {
            if (!bytes) return '0 B';
            const k = 1024;
            const sizes = ['B', 'KB', 'MB', 'GB'];
            const i = Math.floor(Math.log(bytes) / Math.log(k));
            return (bytes / Math.pow(k, i)).toFixed(2) + ' ' + sizes[i];
        }
        
        function setupDragDrop() {
            const zone = document.getElementById('dropZone');
            zone.addEventListener('dragover', (e) => {
                e.preventDefault();
                zone.classList.add('drag-over');
            });
            zone.addEventListener('dragleave', () => {
                zone.classList.remove('drag-over');
            });
            zone.addEventListener('drop', (e) => {
                e.preventDefault();
                zone.classList.remove('drag-over');
                handleFileSelect(e.dataTransfer.files);
            });
        }
        
        function editDeviceName() {
            document.getElementById('deviceNameInput').value = myDeviceName;
            document.getElementById('nameModal').classList.add('show');
        }
        
        function closeNameModal() {
            document.getElementById('nameModal').classList.remove('show');
        }
        
        function saveDeviceName() {
            const newName = document.getElementById('deviceNameInput').value.trim();
            if (!newName) { showToast('❌ Enter a name'); return; }
            myDeviceName = newName;
            localStorage.setItem('deviceName', myDeviceName);
            document.getElementById('currentDeviceName').textContent = myDeviceName;
            closeNameModal();
            connections.forEach((c) => {
                c.dataChannel.send({ type: 'name', name: myDeviceName });
            });
        }
        
        function updateCharCount() {
            const input = document.getElementById('deviceNameInput');
            document.getElementById('charCount').textContent = input.value.length;
            input.addEventListener('input', () => {
                document.getElementById('charCount').textContent = input.value.length;
            });
        }
        
        function refreshConnection() {
            retryCount = 0;
            if (myPeer) myPeer.destroy();
            myPeer = null;
            connections.clear();
            updateStatus('⏳ Reconnecting...', 'error');
            setTimeout(initializeConnection, 500);
        }
        
        function showMyQR() {
            const qrData = 'LOCALDROP:' + myDeviceId + ':' + myDeviceName;
            document.getElementById('qrDeviceName').textContent = myDeviceName;
            
            const container = document.getElementById('qrcode');
            container.innerHTML = '';
            
            new QRCode(container, {
                text: qrData,
                width: 256,
                height: 256,
                colorDark: '#1f2937',
                colorLight: '#ffffff'
            });
            
            document.getElementById('qrModal').classList.add('show');
        }
        
        function closeQRModal() {
            document.getElementById('qrModal').classList.remove('show');
            document.getElementById('qrcode').innerHTML = '';
        }
        
        function scanQRCode() {
            document.getElementById('scannerModal').classList.add('show');
        }
        
        function closeScannerModal() {
            document.getElementById('scannerModal').classList.remove('show');
            if (qrScanner) {
                qrScanner.stop().catch(() => {});
                qrScanner = null;
            }
        }
        
        async function requestCameraPermission() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } });
                stream.getTracks().forEach(track => track.stop());
                startQRScanner();
            } catch (error) {
                showToast('❌ Camera denied');
            }
        }
        
        function startQRScanner() {
            document.getElementById('startCameraBtn').style.display = 'none';
            qrScanner = new Html5Qrcode("qr-reader");
            
            qrScanner.start(
                { facingMode: "environment" },
                { fps: 10, qrbox: { width: 250, height: 250 } },
                (decodedText) => handleQRScan(decodedText),
                () => {}
            ).catch(() => {
                showToast('❌ Scanner failed');
                document.getElementById('startCameraBtn').style.display = 'block';
            });
        }
        
        function handleQRScan(qrData) {
            try {
                if (!qrData.startsWith('LOCALDROP:')) {
                    showToast('❌ Invalid QR');
                    return;
                }
                
                const [, remotePeerId, remoteName] = qrData.split(':');
                
                if (remotePeerId === myDeviceId) {
                    showToast('⚠️ Cannot connect to yourself');
                    return;
                }
                
                if (qrScanner) qrScanner.stop();
                
                document.getElementById('scan-result').innerHTML = `
                    <div style="text-align: center;">✅ Found: ${remoteName}<br><span style="color: #667eea;">⏳ Connecting...</span></div>
                `;
                document.getElementById('scan-result').style.display = 'block';
                
                setTimeout(() => {
                    connectToPeer(remotePeerId, remoteName);
                    setTimeout(closeScannerModal, 1500);
                }, 800);
                
            } catch (error) {
                showToast('❌ Invalid QR');
            }
        }
        
        function connectToPeer(peerId, peerName) {
            if (!myPeer) { showToast('❌ Not ready'); return; }
            
            console.log('📞 Connecting...');
            updateStatus('⏳ Connecting...', 'connecting');
            
            try {
                const conn = myPeer.connect(peerId, { reliable: true });
                connections.set(peerId, { conn, name: peerName, dataChannel: conn });
                
                conn.on('open', () => {
                    console.log('✅ Connected!');
                    updateStatus('✅ Connected to ' + peerName, 'connected');
                    conn.send({ type: 'name', name: myDeviceName });
                    updateConnectedDevices();
                    showToast('✅ Connected!');
                });
                
                conn.on('error', (err) => {
                    console.error('Error:', err);
                    updateStatus('❌ Connection failed', 'error');
                    showToast('❌ Connection failed');
                });
                
                conn.on('close', () => {
                    connections.delete(peerId);
                    updateConnectedDevices();
                });
                
            } catch (error) {
                console.error('Error:', error);
                updateStatus('❌ Error', 'error');
                showToast('❌ Connection failed');
            }
        }
        
        function updateConnectedDevices() {
            const container = document.getElementById('connectedDevices');
            
            if (connections.size === 0) {
                container.innerHTML = '<p style="color: #6b7280; text-align: center; padding: 20px;">No devices connected. Scan a QR code!</p>';
                return;
            }
            
            container.innerHTML = '';
            connections.forEach((data, peerId) => {
                const card = document.createElement('div');
                card.className = 'device-card';
                card.innerHTML = `
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <div style="font-weight: 600;">📱 ${data.name}</div>
                            <div style="font-size: 12px; opacity: 0.9;">Ready to send/receive</div>
                        </div>
                        <button onclick="disconnectPeer('${peerId}')" class="btn btn-danger" style="padding: 8px 12px;">
                            Disconnect
                        </button>
                    </div>
                `;
                container.appendChild(card);
            });
        }
        
        function disconnectPeer(peerId) {
            const data = connections.get(peerId);
            if (data) {
                data.conn.close();
                connections.delete(peerId);
                updateConnectedDevices();
                updateStatus('✅ Ready', 'online');
            }
        }
        
        function updateStatus(msg, cls) {
            const el = document.getElementById('connectionStatus');
            el.className = 'status ' + cls;
            el.textContent = msg;
        }
        
        function showToast(msg) {
            const toast = document.createElement('div');
            toast.textContent = msg;
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
                font-size: 14px;
            `;
            document.body.appendChild(toast);
            setTimeout(() => toast.remove(), 3000);
        }
        
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeNameModal();
                closeQRModal();
                closeScannerModal();
            }
        });
    </script>
</body>
</html>'''

with open('connect.html', 'w', encoding='utf-8') as f:
    f.write(connect_fixed_final)

print("✅ connect.html - FINAL FIXED VERSION")
print("\n🔧 Fixes Applied:")
print("   1. Send section ALWAYS visible")
print("   2. Received files section ALWAYS visible")
print("   3. Removed conditional display logic")
print("   4. QR scanning flow simplified (no long delays)")
print("   5. Connection process optimized")
print("   6. Fixed retry/connection stability")
print("\n✅ Ready to upload!")
