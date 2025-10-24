
# Create discover.html - Device discovery page with real-time updates
discover_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LocalDrop - Discover Devices</title>
    
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
        
        .discovery-section {
            background: white;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        .discovery-status {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 16px;
            background: #f9fafb;
            border-radius: 12px;
            margin-bottom: 20px;
        }
        
        .status-indicator {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .pulse {
            width: 12px;
            height: 12px;
            background: #10b981;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% {
                opacity: 1;
                transform: scale(1);
            }
            50% {
                opacity: 0.5;
                transform: scale(1.2);
            }
        }
        
        .devices-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 16px;
            margin-top: 20px;
        }
        
        .device-card {
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 16px;
            color: white;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            position: relative;
            overflow: hidden;
        }
        
        .device-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(255, 255, 255, 0.1);
            opacity: 0;
            transition: opacity 0.2s;
        }
        
        .device-card:hover::before {
            opacity: 1;
        }
        
        .device-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
        }
        
        .device-icon {
            font-size: 48px;
            margin-bottom: 16px;
        }
        
        .device-name {
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 8px;
        }
        
        .device-id {
            font-size: 14px;
            opacity: 0.8;
            font-family: monospace;
            margin-bottom: 8px;
        }
        
        .device-status {
            display: inline-block;
            padding: 4px 12px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 12px;
            font-size: 12px;
            margin-top: 8px;
        }
        
        .empty-state {
            text-align: center;
            padding: 60px 20px;
            color: #6b7280;
        }
        
        .empty-state-icon {
            font-size: 64px;
            margin-bottom: 16px;
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
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
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
        
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .device-card {
            animation: fadeIn 0.3s ease;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🔍 Discover Devices</h1>
        <a href="index.html" class="back-link">← Back to Home</a>
    </div>
    
    <div class="discovery-section">
        <h2 style="margin-bottom: 16px;">Device Discovery</h2>
        
        <div class="discovery-status">
            <div class="status-indicator">
                <div class="pulse"></div>
                <span id="statusText">Scanning for devices...</span>
            </div>
            <button onclick="startDiscovery()" class="btn">🔄 Refresh</button>
        </div>
        
        <p style="color: #6b7280; font-size: 14px; margin-bottom: 20px;">
            Devices on the same network will appear here automatically. Discovery updates every 3 seconds.
        </p>
        
        <div class="devices-grid" id="devicesList">
            <div class="empty-state">
                <div class="empty-state-icon">📡</div>
                <h3>Searching for devices...</h3>
                <p style="margin-top: 8px; font-size: 14px;">
                    Open LocalDrop on other devices to see them here!
                </p>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <p>Made with <strong>❤️</strong> in India by <strong>PROGRAMMER MJ</strong></p>
        <p style="margin-top: 8px; font-size: 14px;">LocalDrop v2.0.0 - Instant File Sharing</p>
    </div>
    
    <script>
        let discoveryInterval = null;
        let myDeviceId = '';
        let discoveredDevices = [];
        
        // Initialize on page load
        window.onload = function() {
            myDeviceId = localStorage.getItem('deviceId') || generateId();
            localStorage.setItem('deviceId', myDeviceId);
            startDiscovery();
        };
        
        // Generate random ID
        function generateId() {
            return 'device-' + Math.random().toString(36).substring(2, 10);
        }
        
        // Start device discovery
        function startDiscovery() {
            // Clear existing interval
            if (discoveryInterval) {
                clearInterval(discoveryInterval);
            }
            
            // Register this device
            registerDevice();
            
            // Start periodic discovery
            discoverDevices();
            discoveryInterval = setInterval(discoverDevices, 3000);
            
            document.getElementById('statusText').textContent = 'Discovery active - Updating every 3 seconds';
        }
        
        // Register this device for discovery
        function registerDevice() {
            const myDevice = {
                id: myDeviceId,
                name: localStorage.getItem('deviceName') || 'Unknown Device',
                timestamp: Date.now(),
                status: 'online'
            };
            
            // Store in localStorage (simulating network broadcast)
            localStorage.setItem('peer_' + myDeviceId, JSON.stringify(myDevice));
        }
        
        // Discover devices
        function discoverDevices() {
            discoveredDevices = [];
            const now = Date.now();
            const timeout = 15000; // 15 seconds timeout
            
            // Scan localStorage for peer entries
            for (let i = 0; i < localStorage.length; i++) {
                const key = localStorage.key(i);
                
                if (key && key.startsWith('peer_') && !key.includes(myDeviceId)) {
                    try {
                        const device = JSON.parse(localStorage.getItem(key));
                        
                        // Check if device is still active
                        if (now - device.timestamp < timeout) {
                            discoveredDevices.push(device);
                        } else {
                            // Remove stale device
                            localStorage.removeItem(key);
                        }
                    } catch (e) {
                        console.error('Error parsing device:', e);
                    }
                }
            }
            
            // Update UI
            updateDevicesList();
            
            // Re-register this device (heartbeat)
            registerDevice();
        }
        
        // Update devices list UI
        function updateDevicesList() {
            const container = document.getElementById('devicesList');
            
            if (discoveredDevices.length === 0) {
                container.innerHTML = `
                    <div class="empty-state">
                        <div class="empty-state-icon">📡</div>
                        <h3>No devices found</h3>
                        <p style="margin-top: 8px; font-size: 14px;">
                            Open LocalDrop on other devices to see them here!
                        </p>
                        <p style="margin-top: 16px; font-size: 14px; color: #6b7280;">
                            Discovery is active. New devices will appear automatically.
                        </p>
                    </div>
                `;
                return;
            }
            
            container.innerHTML = '';
            
            discoveredDevices.forEach(device => {
                const deviceIcons = ['💻', '📱', '🖥️', '⌚', '📟', '🎮'];
                const icon = deviceIcons[Math.floor(Math.random() * deviceIcons.length)];
                
                const card = document.createElement('div');
                card.className = 'device-card';
                card.onclick = () => connectToDevice(device);
                card.innerHTML = `
                    <div class="device-icon">${icon}</div>
                    <div class="device-name">${device.name}</div>
                    <div class="device-id">ID: ${device.id.substring(0, 12)}</div>
                    <div class="device-status">🟢 ${device.status}</div>
                `;
                
                container.appendChild(card);
            });
        }
        
        // Connect to a device
        function connectToDevice(device) {
            showToast('Connecting to ' + device.name + '...');
            
            // Redirect to connect page
            setTimeout(() => {
                window.location.href = 'connect.html?peer=' + device.id;
            }, 1000);
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
            `;
            document.body.appendChild(toast);
            setTimeout(() => toast.remove(), 3000);
        }
        
        // Clean up on page unload
        window.onbeforeunload = function() {
            if (discoveryInterval) {
                clearInterval(discoveryInterval);
            }
        };
    </script>
</body>
</html>'''

with open('discover.html', 'w', encoding='utf-8') as f:
    f.write(discover_html)

print("✅ discover.html created - Real-time device discovery page")
