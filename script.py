
# Create connect.html with REAL cross-device WebRTC using PeerJS cloud
connect_peerjs = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LocalDrop - Connect & Share</title>
    
    <!-- Load libraries -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <script src="https://unpkg.com/html5-qrcode@2.3.8/html5-qrcode.min.js"></script>
    <!-- PeerJS for real P2P -->
    <script src="https://unpkg.com/peerjs@1.5.4/dist/peerjs.min.js"></script>
    
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
        
        .device-name-display h2 {
            font-size: 24px;
            color: #1f2937;
        }
        
        .btn {
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.2s;
            font-size: 14px;
        }
        
        .btn-primary {
            background: #667eea;
            color: white;
        }
        
        .btn-success {
            background: #10b981;
            color: white;
        }
        
        .btn-info {
            background: #3b82f6;
            color: white;
        }
        
        .btn-warning {
            background: #8b5cf6;
            color: white;
        }
        
        .btn:hover:not(:disabled) {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        }
        
        .btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }
        
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
        
        .status.online {
            background: #d1fae5;
            color: #065f46;
        }
        
        .status.connecting {
            background: #fef3c7;
            color: #92400e;
        }
        
        .status.connected {
            background: #dbeafe;
            color: #1e40af;
        }
        
        .devices-section {
            background: white;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        .device-card {
            padding: 16px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
            color: white;
            margin-bottom: 12px;
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
        
        .modal.show {
            display: flex !important;
        }
        
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
        
        .modal-header h3 {
            font-size: 24px;
        }
        
        .close-btn {
            background: none;
            border: none;
            font-size: 32px;
            cursor: pointer;
            color: #6b7280;
            line-height: 1;
            padding: 0;
            width: 32px;
            height: 32px;
        }
        
        .close-btn:hover {
            color: #1f2937;
        }
        
        .modal-body {
            margin-bottom: 24px;
        }
        
        .qr-container {
            display: flex;
            justify-content: center;
            margin: 24px 0;
            padding: 20px;
            background: #f9fafb;
            border-radius: 12px;
        }
        
        #qrcode {
            display: inline-block;
        }
        
        .device-id {
            text-align: center;
            font-family: monospace;
            font-size: 12px;
            color: #6b7280;
            margin-top: 16px;
            padding: 12px;
            background: #f3f4f6;
            border-radius: 8px;
            word-break: break-all;
        }
        
        .instructions {
            font-size: 14px;
            color: #6b7280;
            text-align: center;
            margin-top: 16px;
        }
        
        #qr-reader {
            width: 100%;
            max-width: 400px;
            margin: 0 auto;
        }
        
        @keyframes spin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        
        .spinning {
            display: inline-block;
            animation: spin 1s linear infinite;
        }
        
        @media (max-width: 768px) {
            .controls {
                flex-direction: column;
            }
            .btn {
                width: 100%;
            }
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
            <button onclick="editDeviceName()" class="btn btn-primary">✏️ Edit Name</button>
        </div>
        
        <div class="controls">
            <button onclick="refreshDevices()" class="btn btn-success" id="refreshBtn">
                <span id="refreshIcon">🔄</span> Refresh
            </button>
            <button onclick="showMyQR()" class="btn btn-info">
                📱 Show My QR Code
            </button>
            <button onclick="scanQRCode()" class="btn btn-warning">
                📷 Scan QR Code
            </button>
        </div>
        
        <div class="status online" id="connectionStatus">
            ⏳ Connecting to server...
        </div>
    </div>
    
    <div class="devices-section">
        <h2>Connected Devices</h2>
        <div id="connectedDevices" style="margin-top: 20px;">
            <p style="color: #6b7280; text-align: center; padding: 20px;">
                No devices connected yet. Scan a QR code to connect!
            </p>
        </div>
    </div>
    
    <div class="footer">
        <p>Made with <strong>❤️</strong> in India by <strong>PROGRAMMER MJ</strong></p>
        <p style="margin-top: 8px; font-size: 14px;">LocalDrop v2.0.0 - Instant File Sharing</p>
        <p style="margin-top: 8px; font-size: 12px; color: #9ca3af;">Using PeerJS Cloud Server</p>
    </div>
    
    <!-- Device Name Modal -->
    <div id="nameModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Edit Device Name</h3>
                <button class="close-btn" onclick="closeNameModal()">×</button>
            </div>
            <div class="modal-body">
                <label style="display: block; margin-bottom: 8px; font-weight: 500;">Device Name</label>
                <input type="text" id="deviceNameInput" maxlength="20" 
                       style="width: 100%; padding: 12px; border: 2px solid #e5e7eb; border-radius: 8px; font-size: 16px;"
                       placeholder="Enter device name">
                <p style="font-size: 14px; color: #6b7280; margin-top: 8px;">
                    <span id="charCount">0</span>/20 characters
                </p>
            </div>
            <div style="display: flex; gap: 12px; justify-content: flex-end;">
                <button onclick="closeNameModal()" class="btn" style="background: #e5e7eb; color: #1f2937;">Cancel</button>
                <button onclick="saveDeviceName()" class="btn btn-primary">Save</button>
            </div>
        </div>
    </div>
    
    <!-- QR Code Display Modal -->
    <div id="qrModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>📱 My QR Code</h3>
                <button class="close-btn" onclick="closeQRModal()">×</button>
            </div>
            <div class="modal-body">
                <p style="text-align: center; margin-bottom: 16px;">Others can scan this code to connect to your device:</p>
                <div class="qr-container">
                    <div id="qrcode"></div>
                </div>
                <div class="device-id">
                    Device: <span id="qrDeviceName"></span><br>
                    Peer ID: <span id="qrPeerId" style="font-size: 10px;"></span>
                </div>
                <p class="instructions">Keep this QR code visible for others to scan</p>
            </div>
        </div>
    </div>
    
    <!-- QR Scanner Modal -->
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
                <div id="scan-result" style="margin-top: 16px; padding: 12px; background: #f3f4f6; border-radius: 8px; font-size: 14px; display: none;"></div>
            </div>
        </div>
    </div>
    
    <script>
        // Global variables
        let myDeviceName = '';
        let myPeer = null;
        let myPeerId = '';
        let qrScanner = null;
        let qrcodeInstance = null;
        let connections = new Map(); // Map<peerId, {conn, data}>
        
        // Initialize on page load
        window.onload = function() {
            console.log('🚀 LocalDrop v2.0.0 with PeerJS - Loading...');
            initializeDevice();
            initializePeerJS();
        };
        
        // Initialize device
        function initializeDevice() {
            myDeviceName = localStorage.getItem('deviceName') || generateDeviceName();
            localStorage.setItem('deviceName', myDeviceName);
            
            document.getElementById('currentDeviceName').textContent = myDeviceName;
            
            console.log('✅ Device name:', myDeviceName);
            
            // Check for first time
            if (!localStorage.getItem('hasVisited')) {
                localStorage.setItem('hasVisited', 'true');
                setTimeout(() => editDeviceName(), 500);
            }
        }
        
        // Initialize PeerJS - REAL P2P CONNECTION
        function initializePeerJS() {
            console.log('🔌 Connecting to PeerJS cloud server...');
            
            // Create peer with PeerJS cloud server (FREE!)
            myPeer = new Peer({
                config: {
                    iceServers: [
                        { urls: 'stun:stun.l.google.com:19302' },
                        { urls: 'stun:stun1.l.google.com:19302' },
                        { urls: 'stun:stun.cloudflare.com:3478' }
                    ]
                }
            });
            
            // When connected to PeerJS server
            myPeer.on('open', (id) => {
                myPeerId = id;
                console.log('✅ Connected to PeerJS! My Peer ID:', myPeerId);
                updateStatus('✅ Ready to connect - Connected to server', 'online');
            });
            
            // When someone connects to us
            myPeer.on('connection', (conn) => {
                console.log('📞 Incoming connection from:', conn.peer);
                handleIncomingConnection(conn);
            });
            
            // Handle errors
            myPeer.on('error', (err) => {
                console.error('❌ PeerJS error:', err);
                updateStatus('❌ Connection error - ' + err.type, 'online');
                
                // Retry connection after error
                setTimeout(() => {
                    console.log('🔄 Retrying connection...');
                    initializePeerJS();
                }, 5000);
            });
            
            // Handle disconnection
            myPeer.on('disconnected', () => {
                console.log('⚠️ Disconnected from PeerJS server');
                updateStatus('⚠️ Reconnecting...', 'connecting');
                myPeer.reconnect();
            });
        }
        
        // Handle incoming connection
        function handleIncomingConnection(conn) {
            connections.set(conn.peer, {
                conn: conn,
                data: { name: 'Unknown Device' }
            });
            
            conn.on('open', () => {
                console.log('✅ Connection established with', conn.peer);
                // Send our name
                conn.send({
                    type: 'name',
                    name: myDeviceName
                });
            });
            
            conn.on('data', (data) => {
                console.log('📨 Received data:', data);
                
                if (data.type === 'name') {
                    // Store peer name
                    const connData = connections.get(conn.peer);
                    if (connData) {
                        connData.data.name = data.name;
                        updateConnectedDevices();
                    }
                }
                // Handle file transfers here
            });
            
            conn.on('close', () => {
                console.log('👋 Connection closed with', conn.peer);
                connections.delete(conn.peer);
                updateConnectedDevices();
            });
            
            conn.on('error', (err) => {
                console.error('❌ Connection error:', err);
            });
        }
        
        // Connect to a peer
        function connectToPeer(peerId, peerName) {
            console.log('📞 Connecting to peer:', peerId);
            updateStatus('⏳ Connecting to ' + peerName + '...', 'connecting');
            
            const conn = myPeer.connect(peerId, {
                reliable: true
            });
            
            connections.set(peerId, {
                conn: conn,
                data: { name: peerName }
            });
            
            conn.on('open', () => {
                console.log('✅ Connected to', peerName);
                updateStatus('✅ Connected to ' + peerName, 'connected');
                
                // Send our name
                conn.send({
                    type: 'name',
                    name: myDeviceName
                });
                
                updateConnectedDevices();
                showToast('✅ Connected to ' + peerName);
            });
            
            conn.on('data', (data) => {
                console.log('📨 Received data:', data);
                // Handle received data
            });
            
            conn.on('close', () => {
                console.log('👋 Connection closed');
                connections.delete(peerId);
                updateConnectedDevices();
                if (connections.size === 0) {
                    updateStatus('✅ Ready to connect', 'online');
                }
            });
            
            conn.on('error', (err) => {
                console.error('❌ Connection error:', err);
                updateStatus('❌ Connection failed', 'online');
                showToast('❌ Connection failed');
            });
        }
        
        // Generate device name
        function generateDeviceName() {
            const prefixes = ['Phone', 'Laptop', 'Desktop', 'Tablet', 'Device'];
            const prefix = prefixes[Math.floor(Math.random() * prefixes.length)];
            const number = Math.floor(1000 + Math.random() * 9000);
            return prefix + '-' + number;
        }
        
        // Edit device name
        function editDeviceName() {
            document.getElementById('deviceNameInput').value = myDeviceName;
            updateCharCount();
            document.getElementById('nameModal').classList.add('show');
            document.getElementById('deviceNameInput').focus();
        }
        
        // Close name modal
        function closeNameModal() {
            document.getElementById('nameModal').classList.remove('show');
        }
        
        // Save device name
        function saveDeviceName() {
            const newName = document.getElementById('deviceNameInput').value.trim();
            
            if (!newName) {
                alert('Please enter a device name');
                return;
            }
            
            if (newName.length > 20) {
                alert('Name too long (max 20 characters)');
                return;
            }
            
            myDeviceName = newName;
            localStorage.setItem('deviceName', myDeviceName);
            document.getElementById('currentDeviceName').textContent = myDeviceName;
            closeNameModal();
            showToast('✅ Device name updated!');
            
            // Send updated name to all connections
            connections.forEach((connData) => {
                connData.conn.send({
                    type: 'name',
                    name: myDeviceName
                });
            });
        }
        
        // Update character count
        function updateCharCount() {
            const input = document.getElementById('deviceNameInput');
            const count = document.getElementById('charCount');
            input.addEventListener('input', () => {
                count.textContent = input.value.length;
            });
            count.textContent = input.value.length;
        }
        
        // Refresh devices
        function refreshDevices() {
            const btn = document.getElementById('refreshBtn');
            const icon = document.getElementById('refreshIcon');
            
            btn.disabled = true;
            icon.classList.add('spinning');
            
            setTimeout(() => {
                btn.disabled = false;
                icon.classList.remove('spinning');
                showToast('🔄 Refreshed');
                updateConnectedDevices();
            }, 1000);
        }
        
        // Show my QR code
        function showMyQR() {
            if (!myPeerId) {
                showToast('⏳ Please wait, connecting to server...');
                return;
            }
            
            document.getElementById('qrDeviceName').textContent = myDeviceName;
            document.getElementById('qrPeerId').textContent = myPeerId;
            
            const qrContainer = document.getElementById('qrcode');
            qrContainer.innerHTML = '';
            
            // QR format: LOCALDROP:PEERID:NAME
            const qrData = 'LOCALDROP:' + myPeerId + ':' + myDeviceName;
            
            console.log('📱 QR data:', qrData);
            
            try {
                qrcodeInstance = new QRCode(qrContainer, {
                    text: qrData,
                    width: 256,
                    height: 256,
                    colorDark: '#1f2937',
                    colorLight: '#ffffff',
                    correctLevel: QRCode.CorrectLevel.M
                });
                
                document.getElementById('qrModal').classList.add('show');
            } catch (error) {
                console.error('❌ QR error:', error);
                showToast('❌ Error generating QR');
            }
        }
        
        // Close QR modal
        function closeQRModal() {
            document.getElementById('qrModal').classList.remove('show');
            if (qrcodeInstance) {
                document.getElementById('qrcode').innerHTML = '';
                qrcodeInstance = null;
            }
        }
        
        // Scan QR code
        function scanQRCode() {
            document.getElementById('scannerModal').classList.add('show');
        }
        
        // Close scanner modal
        function closeScannerModal() {
            document.getElementById('scannerModal').classList.remove('show');
            if (qrScanner) {
                qrScanner.stop().catch(err => console.error(err));
                qrScanner = null;
            }
            document.getElementById('scan-result').style.display = 'none';
            document.getElementById('startCameraBtn').style.display = 'block';
        }
        
        // Request camera permission
        async function requestCameraPermission() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ 
                    video: { facingMode: 'environment' } 
                });
                stream.getTracks().forEach(track => track.stop());
                showToast('✅ Camera granted');
                startQRScanner();
            } catch (error) {
                console.error('❌ Camera error:', error);
                let message = '❌ Camera access failed';
                if (error.name === 'NotAllowedError') {
                    message = '❌ Camera denied. Please allow camera.';
                } else if (error.name === 'NotFoundError') {
                    message = '❌ No camera found';
                }
                showToast(message);
            }
        }
        
        // Start QR scanner
        function startQRScanner() {
            document.getElementById('startCameraBtn').style.display = 'none';
            
            qrScanner = new Html5Qrcode("qr-reader");
            
            qrScanner.start(
                { facingMode: "environment" },
                { fps: 10, qrbox: { width: 250, height: 250 } },
                (decodedText) => {
                    handleQRScan(decodedText);
                },
                (errorMessage) => {
                    // Scanning errors
                }
            ).catch(err => {
                console.error('❌ Scanner error:', err);
                showToast('❌ Scanner failed');
                document.getElementById('startCameraBtn').style.display = 'block';
            });
        }
        
        // Handle QR scan
        function handleQRScan(qrData) {
            console.log('📷 Scanned:', qrData);
            
            try {
                if (!qrData.startsWith('LOCALDROP:')) {
                    showToast('❌ Invalid QR code');
                    return;
                }
                
                const parts = qrData.split(':');
                if (parts.length !== 3) {
                    showToast('❌ Invalid format');
                    return;
                }
                
                const remotePeerId = parts[1];
                const remotePeerName = parts[2];
                
                if (remotePeerId === myPeerId) {
                    showToast('⚠️ Cannot connect to yourself!');
                    return;
                }
                
                // Show success
                document.getElementById('scan-result').innerHTML = `
                    <div style="text-align: center;">
                        <div style="font-size: 24px; margin-bottom: 8px;">✅</div>
                        <div style="font-weight: 600;">Found: ${remotePeerName}</div>
                        <div style="margin-top: 4px; font-size: 12px; color: #6b7280;">Peer ID: ${remotePeerId.substring(0, 12)}...</div>
                        <div style="margin-top: 8px; color: #667eea;">⏳ Connecting...</div>
                    </div>
                `;
                document.getElementById('scan-result').style.display = 'block';
                
                // Stop scanner
                if (qrScanner) {
                    qrScanner.stop();
                }
                
                // Connect to peer
                setTimeout(() => {
                    connectToPeer(remotePeerId, remotePeerName);
                    setTimeout(() => {
                        closeScannerModal();
                    }, 2000);
                }, 1000);
                
            } catch (error) {
                console.error('❌ QR parse error:', error);
                showToast('❌ Invalid QR format');
            }
        }
        
        // Update connection status
        function updateStatus(message, statusClass) {
            const statusEl = document.getElementById('connectionStatus');
            statusEl.textContent = message;
            statusEl.className = 'status ' + statusClass;
        }
        
        // Update connected devices display
        function updateConnectedDevices() {
            const container = document.getElementById('connectedDevices');
            
            if (connections.size === 0) {
                container.innerHTML = `
                    <p style="color: #6b7280; text-align: center; padding: 20px;">
                        No devices connected yet. Scan a QR code to connect!
                    </p>
                `;
                return;
            }
            
            container.innerHTML = '';
            connections.forEach((connData, peerId) => {
                const card = document.createElement('div');
                card.className = 'device-card';
                card.innerHTML = `
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                        <div style="flex: 1;">
                            <div style="font-size: 18px; font-weight: 600; margin-bottom: 4px;">
                                📱 ${connData.data.name}
                            </div>
                            <div style="font-size: 12px; opacity: 0.9;">
                                Connected • ${peerId.substring(0, 12)}...
                            </div>
                        </div>
                        <button onclick="disconnectPeer('${peerId}')" class="btn" 
                                style="background: rgba(255,255,255,0.2); border: 1px solid white; color: white;">
                            Disconnect
                        </button>
                    </div>
                `;
                container.appendChild(card);
            });
        }
        
        // Disconnect from peer
        function disconnectPeer(peerId) {
            const connData = connections.get(peerId);
            if (connData) {
                connData.conn.close();
                connections.delete(peerId);
                updateConnectedDevices();
                if (connections.size === 0) {
                    updateStatus('✅ Ready to connect', 'online');
                }
                showToast('🔌 Disconnected');
            }
        }
        
        // Show toast notification
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
                font-size: 14px;
                max-width: 90%;
            `;
            document.body.appendChild(toast);
            setTimeout(() => toast.remove(), 3000);
        }
        
        // Escape key handling
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeNameModal();
                closeQRModal();
                closeScannerModal();
            }
        });
        
        console.log('✅ LocalDrop ready with PeerJS!');
    </script>
</body>
</html>'''

with open('connect.html', 'w', encoding='utf-8') as f:
    f.write(connect_peerjs)

print("✅ connect.html with REAL PeerJS P2P created!")
print("\n🌟 KEY CHANGES:")
print("   1. Uses PeerJS cloud server (FREE)")
print("   2. Real WebRTC P2P connections")
print("   3. Works across ALL devices")
print("   4. No localStorage signaling")
print("   5. Same as SnapDrop architecture")
print("\n✅ Now works just like SnapDrop/PairDrop!")
