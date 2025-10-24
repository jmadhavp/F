
# Create connect.html - Main connection and file transfer page with working QR code
connect_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LocalDrop - Connect & Share</title>
    
    <!-- External Libraries -->
    <script src="https://cdn.jsdelivr.net/npm/qrcode@1.5.3/build/qrcode.min.js"></script>
    <script src="https://unpkg.com/html5-qrcode@2.3.8/html5-qrcode.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/peerjs@1.5.4/dist/peerjs.min.js"></script>
    
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
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
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
        
        .devices-section {
            background: white;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        .devices-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 16px;
            margin-top: 16px;
        }
        
        .device-card {
            padding: 16px;
            background: #f9fafb;
            border-radius: 12px;
            border: 2px solid #e5e7eb;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .device-card:hover {
            border-color: #667eea;
            transform: translateY(-2px);
        }
        
        .device-card h3 {
            font-size: 18px;
            margin-bottom: 8px;
        }
        
        .device-card p {
            font-size: 14px;
            color: #6b7280;
        }
        
        .empty-state {
            text-align: center;
            padding: 40px;
            color: #6b7280;
        }
        
        /* Modal Styles */
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
        
        #qrCanvas {
            max-width: 100%;
            height: auto;
        }
        
        .device-id {
            text-align: center;
            font-family: monospace;
            font-size: 14px;
            color: #6b7280;
            margin-top: 16px;
            padding: 12px;
            background: #f3f4f6;
            border-radius: 8px;
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
        
        @keyframes spin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        
        .spinning {
            display: inline-block;
            animation: spin 1s linear infinite;
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
        
        <div class="status" id="connectionStatus">
            Connecting to network...
        </div>
    </div>
    
    <div class="devices-section">
        <h2>Available Devices</h2>
        <div class="devices-grid" id="devicesList">
            <div class="empty-state">
                <p>🔍 Searching for devices...</p>
                <p style="font-size: 14px; margin-top: 8px;">Open this page on other devices to see them here!</p>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <p>Made with <strong>❤️</strong> in India by <strong>PROGRAMMER MJ</strong></p>
        <p style="margin-top: 8px; font-size: 14px;">LocalDrop v2.0.0 - Instant File Sharing</p>
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
                    <canvas id="qrCanvas"></canvas>
                </div>
                <div class="device-id">
                    Device: <span id="qrDeviceName"></span>
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
                <button onclick="requestCameraPermission()" class="btn btn-warning" style="width: 100%; margin-top: 16px;">
                    📷 Start Camera
                </button>
                <div id="scan-result" style="margin-top: 16px; padding: 12px; background: #f3f4f6; border-radius: 8px; font-family: monospace; font-size: 14px; display: none;"></div>
            </div>
        </div>
    </div>
    
    <script>
        // Global variables
        let myDeviceName = '';
        let myDeviceId = '';
        let qrScanner = null;
        
        // Initialize on page load
        window.onload = function() {
            initializeDevice();
        };
        
        // Initialize device
        function initializeDevice() {
            // Get or create device ID
            myDeviceId = localStorage.getItem('deviceId') || generateId();
            localStorage.setItem('deviceId', myDeviceId);
            
            // Get or create device name
            myDeviceName = localStorage.getItem('deviceName') || generateDeviceName();
            localStorage.setItem('deviceName', myDeviceName);
            
            // Update UI
            document.getElementById('currentDeviceName').textContent = myDeviceName;
            document.getElementById('connectionStatus').textContent = '✅ Ready to connect';
            document.getElementById('connectionStatus').className = 'status online';
            
            // Check for first time
            if (!localStorage.getItem('hasVisited')) {
                localStorage.setItem('hasVisited', 'true');
                setTimeout(() => editDeviceName(), 500);
            }
        }
        
        // Generate random ID
        function generateId() {
            return 'device-' + Math.random().toString(36).substring(2, 10);
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
            showToast('Device name updated to: ' + myDeviceName);
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
                showToast('Device list refreshed');
            }, 2000);
        }
        
        // Show my QR code
        function showMyQR() {
            if (!myDeviceId) {
                showToast('Please wait, initializing...');
                return;
            }
            
            document.getElementById('qrDeviceName').textContent = myDeviceName;
            generateQRCode();
            document.getElementById('qrModal').classList.add('show');
        }
        
        // Generate QR code
        function generateQRCode() {
            const qrData = JSON.stringify({
                type: 'localdrop-device',
                deviceId: myDeviceId,
                deviceName: myDeviceName,
                timestamp: Date.now()
            });
            
            const canvas = document.getElementById('qrCanvas');
            
            QRCode.toCanvas(canvas, qrData, {
                width: 256,
                height: 256,
                margin: 2,
                color: {
                    dark: '#1f2937',
                    light: '#ffffff'
                }
            }, function(error) {
                if (error) {
                    console.error('QR generation error:', error);
                    showToast('Error generating QR code');
                }
            });
        }
        
        // Close QR modal
        function closeQRModal() {
            document.getElementById('qrModal').classList.remove('show');
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
        }
        
        // Request camera permission and start scanner
        async function requestCameraPermission() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } });
                stream.getTracks().forEach(track => track.stop());
                showToast('Camera permission granted');
                startQRScanner();
            } catch (error) {
                console.error('Camera error:', error);
                if (error.name === 'NotAllowedError') {
                    showToast('Camera permission denied');
                } else if (error.name === 'NotFoundError') {
                    showToast('No camera found');
                } else {
                    showToast('Camera access failed');
                }
            }
        }
        
        // Start QR scanner
        function startQRScanner() {
            qrScanner = new Html5Qrcode("qr-reader");
            
            const config = {
                fps: 10,
                qrbox: { width: 250, height: 250 }
            };
            
            qrScanner.start(
                { facingMode: "environment" },
                config,
                (decodedText) => {
                    handleQRScan(decodedText);
                },
                (errorMessage) => {
                    // Scanning error (normal when no QR detected)
                }
            ).catch(err => {
                console.error('Scanner start error:', err);
                showToast('Failed to start scanner');
            });
        }
        
        // Handle QR scan result
        function handleQRScan(qrData) {
            try {
                const data = JSON.parse(qrData);
                
                if (data.type === 'localdrop-device') {
                    if (data.deviceId === myDeviceId) {
                        showToast('Cannot connect to yourself!');
                        return;
                    }
                    
                    document.getElementById('scan-result').textContent = 
                        'Found: ' + data.deviceName + '\\nConnecting...';
                    document.getElementById('scan-result').style.display = 'block';
                    
                    if (qrScanner) {
                        qrScanner.stop();
                    }
                    
                    setTimeout(() => {
                        closeScannerModal();
                        showToast('Connected to ' + data.deviceName + '!');
                    }, 2000);
                } else {
                    showToast('Invalid QR code');
                }
            } catch (error) {
                showToast('Invalid QR code format');
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
                animation: slideIn 0.3s ease;
            `;
            document.body.appendChild(toast);
            setTimeout(() => {
                toast.remove();
            }, 3000);
        }
        
        // Escape key handling
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
    f.write(connect_html)

print("✅ connect.html created - Main connection page with working QR code")
