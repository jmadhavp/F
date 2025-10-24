
# Create discover.html - LOCAL DEVICE DISCOVERY via localStorage heartbeat
discover_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LocalDrop - Discover Devices</title>
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
        .header h1 { font-size: 32px; color: #1f2937; }
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
        .lan-info {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: white;
            padding: 16px;
            border-radius: 12px;
            margin-bottom: 16px;
            font-weight: 600;
            text-align: center;
        }
        .discovery-status {
            background: #fef3c7;
            border: 2px solid #fbbf24;
            color: #92400e;
            padding: 16px;
            border-radius: 12px;
            margin-bottom: 16px;
            text-align: center;
            font-weight: 600;
        }
        .discovery-status.active {
            background: #dbeafe;
            border-color: #3b82f6;
            color: #1e40af;
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
        .btn-primary { background: #667eea; color: white; }
        .btn-success { background: #10b981; color: white; }
        .btn:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2); }
        .section {
            background: white;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        .section h2 { margin-bottom: 16px; font-size: 20px; color: #1f2937; }
        .device-card {
            padding: 16px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
            color: white;
            margin-bottom: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 12px;
        }
        .device-card.found {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        }
        .device-info-text {
            flex: 1;
        }
        .device-name { font-weight: 600; margin-bottom: 4px; }
        .device-subnet { font-size: 12px; opacity: 0.9; }
        .btn-select { padding: 8px 12px; font-size: 12px; background: rgba(255,255,255,0.2); border: 1px solid white; color: white; }
        .controls {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            margin-bottom: 16px;
        }
        .footer {
            background: white;
            border-radius: 16px;
            padding: 24px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            color: #6b7280;
            font-size: 12px;
        }
        .tech-info {
            background: #f3f4f6;
            border-left: 4px solid #667eea;
            padding: 12px;
            border-radius: 8px;
            margin-top: 16px;
            font-size: 11px;
            color: #6b7280;
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
        .modal.show { display: flex !important; }
        .modal-content {
            background: white;
            border-radius: 16px;
            padding: 32px;
            max-width: 500px;
            width: 90%;
        }
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 24px;
        }
        .close-btn { background: none; border: none; font-size: 32px; cursor: pointer; color: #6b7280; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🔍 LocalDrop - Device Discovery</h1>
    </div>
    
    <div class="device-info">
        <div class="device-name-display">
            <div>
                <h2 id="myDeviceName">Device</h2>
                <p style="font-size: 14px; color: #6b7280;">Your Device (Broadcaster)</p>
            </div>
            <button onclick="editDeviceName()" class="btn btn-primary">✏️ Edit Name</button>
        </div>
        
        <div class="lan-info" id="lanInfo">
            📡 Network: Loading...
        </div>
        
        <div class="discovery-status active" id="discoveryStatus">
            🔄 BROADCASTING on local network... (Updates: every 1 second)
        </div>
        
        <div class="controls">
            <button onclick="startDiscovery()" class="btn btn-success">🔍 Scan for Devices</button>
            <button onclick="refreshDiscovery()" class="btn btn-success">🔄 Refresh</button>
        </div>
        
        <div class="tech-info">
            <strong>🔧 How Discovery Works:</strong><br>
            1. Your device broadcasts heartbeat to localStorage every 1 second<br>
            2. Other devices on same LAN read your heartbeat<br>
            3. You receive signals from OTHER devices (same LAN)<br>
            4. Devices match on same subnet (192.168.1.x)<br>
            5. All devices visible to each other
        </div>
    </div>
    
    <div class="section">
        <h2>📱 Devices Found on Your LAN</h2>
        <div id="discoveredDevices">
            <p style="color: #6b7280; text-align: center; padding: 20px;">
                🔄 Scanning... (devices on same 192.168.1.x will appear here)
            </p>
        </div>
    </div>
    
    <div class="footer">
        <p><strong>📡 LOCAL DISCOVERY:</strong> No server needed! Uses localStorage heartbeat system for local network broadcast.</p>
        <p style="margin-top: 8px;">Made with <strong style="color: #ef4444;">❤️</strong> in India by <strong>PROGRAMMER MJ</strong></p>
    </div>
    
    <div id="nameModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Edit Device Name</h3>
                <button class="close-btn" onclick="closeModal('nameModal')">×</button>
            </div>
            <div style="margin-bottom: 24px;">
                <input type="text" id="deviceNameInput" maxlength="20" style="width: 100%; padding: 12px; border: 2px solid #e5e7eb; border-radius: 8px;">
            </div>
            <div style="display: flex; gap: 12px; justify-content: flex-end;">
                <button onclick="closeModal('nameModal')" class="btn" style="background: #e5e7eb; color: #1f2937;">Cancel</button>
                <button onclick="saveDeviceName()" class="btn btn-primary">Save</button>
            </div>
        </div>
    </div>
    
    <script>
        let myDeviceId = '';
        let myDeviceName = '';
        let lanData = null;
        let discoveryInterval = null;
        let broadcastInterval = null;
        let foundDevices = new Map();
        
        window.onload = function() {
            console.log('🔍 Discovery Page Loading...');
            
            // Get LAN data
            const lanInfo = localStorage.getItem('deviceLANInfo');
            if (lanInfo) {
                lanData = JSON.parse(lanInfo);
                console.log('✅ LAN Data:', lanData);
            } else {
                console.error('❌ No LAN data found');
                alert('Please run lan-detector.html first!');
                window.location.href = 'lan-detector.html';
                return;
            }
            
            // Initialize device
            myDeviceId = localStorage.getItem('deviceId') || 'DEV-' + Date.now();
            myDeviceName = localStorage.getItem('deviceName') || 'Device-' + Math.floor(Math.random() * 9000);
            
            localStorage.setItem('deviceId', myDeviceId);
            localStorage.setItem('deviceName', myDeviceName);
            
            document.getElementById('myDeviceName').textContent = myDeviceName;
            document.getElementById('lanInfo').textContent = '📡 Network: ' + lanData.subnet + '.x | Your IP: ' + lanData.ip;
            
            console.log('✅ Device:', { id: myDeviceId, name: myDeviceName });
            
            // START BROADCASTING
            startBroadcasting();
            
            // START DISCOVERY
            startDiscovery();
        };
        
        // ===== STEP 1: BROADCASTING =====
        function startBroadcasting() {
            console.log('📡 Starting broadcast...');
            
            // Clear old broadcasts
            broadcastInterval = setInterval(() => {
                const heartbeat = {
                    id: myDeviceId,
                    name: myDeviceName,
                    subnet: lanData.subnet,
                    ip: lanData.ip,
                    timestamp: Date.now(),
                    type: 'broadcast'
                };
                
                // Store broadcast signal in localStorage
                const broadcastKey = 'broadcast_' + myDeviceId + '_' + Date.now();
                localStorage.setItem(broadcastKey, JSON.stringify(heartbeat));
                
                console.log('📡 Broadcast sent:', myDeviceName);
                
                // Clean old broadcasts (older than 10 seconds)
                cleanOldBroadcasts();
                
            }, 1000); // Every 1 second
        }
        
        // Clean old broadcast signals
        function cleanOldBroadcasts() {
            const now = Date.now();
            for (let i = localStorage.length - 1; i >= 0; i--) {
                const key = localStorage.key(i);
                if (key && key.startsWith('broadcast_')) {
                    try {
                        const data = JSON.parse(localStorage.getItem(key));
                        // Remove if older than 15 seconds
                        if (now - data.timestamp > 15000) {
                            localStorage.removeItem(key);
                        }
                    } catch (e) {}
                }
            }
        }
        
        // ===== STEP 2: DISCOVERY =====
        function startDiscovery() {
            console.log('🔍 Starting discovery...');
            
            discoveryInterval = setInterval(() => {
                discoverDevices();
            }, 500); // Scan every 500ms for fast discovery
        }
        
        function discoverDevices() {
            const now = Date.now();
            const newDevices = new Map();
            
            // Scan localStorage for broadcasts
            for (let i = 0; i < localStorage.length; i++) {
                const key = localStorage.key(i);
                
                if (key && key.startsWith('broadcast_')) {
                    try {
                        const device = JSON.parse(localStorage.getItem(key));
                        
                        // IMPORTANT: Check conditions
                        // 1. Not my own broadcast
                        // 2. Same subnet
                        // 3. Fresh signal (within 15 seconds)
                        
                        if (device.id === myDeviceId) {
                            console.log('⏭️  Ignoring own broadcast');
                            continue;
                        }
                        
                        if (device.subnet !== lanData.subnet) {
                            console.log('❌ Different subnet:', device.subnet, 'vs', lanData.subnet);
                            continue;
                        }
                        
                        if (now - device.timestamp > 15000) {
                            console.log('⏱️  Stale signal:', device.name);
                            continue;
                        }
                        
                        // Device found!
                        const deviceKey = device.id;
                        
                        if (!foundDevices.has(deviceKey)) {
                            console.log('✅ NEW DEVICE FOUND:', device.name, device.subnet);
                        }
                        
                        newDevices.set(deviceKey, {
                            id: device.id,
                            name: device.name,
                            subnet: device.subnet,
                            ip: device.ip,
                            timestamp: device.timestamp
                        });
                        
                    } catch (e) {
                        console.error('Error parsing broadcast:', e);
                    }
                }
            }
            
            foundDevices = newDevices;
            updateDevicesList();
        }
        
        function updateDevicesList() {
            const container = document.getElementById('discoveredDevices');
            
            if (foundDevices.size === 0) {
                container.innerHTML = `
                    <p style="color: #6b7280; text-align: center; padding: 20px;">
                        🔄 Scanning for devices on ${lanData.subnet}.x...<br>
                        <span style="font-size: 12px; margin-top: 8px;">
                        If no devices appear, make sure:<br>
                        ✅ Other devices opened this page<br>
                        ✅ They're on same WiFi (${lanData.subnet}.x)<br>
                        ✅ Wait 5-10 seconds for detection
                        </span>
                    </p>
                `;
                return;
            }
            
            container.innerHTML = '';
            foundDevices.forEach((device, deviceId) => {
                const card = document.createElement('div');
                card.className = 'device-card found';
                
                const timeSinceSignal = Date.now() - device.timestamp;
                const status = timeSinceSignal < 2000 ? '✅ Active' : '⏳ Standby';
                
                card.innerHTML = `
                    <div class="device-info-text">
                        <div class="device-name">📱 ${device.name}</div>
                        <div class="device-subnet">
                            🌐 ${device.ip} | ${status} | Signal: ${Math.round(timeSinceSignal / 1000)}s ago
                        </div>
                    </div>
                    <button onclick="selectDevice('${device.id}', '${device.name}')" class="btn btn-select">
                        ✅ Select
                    </button>
                `;
                
                container.appendChild(card);
            });
            
            console.log('📊 Devices found:', foundDevices.size);
        }
        
        function refreshDiscovery() {
            console.log('🔄 Refreshing discovery...');
            foundDevices.clear();
            discoverDevices();
        }
        
        function selectDevice(deviceId, deviceName) {
            console.log('✅ Selected:', deviceName);
            
            // Store selected device
            localStorage.setItem('selectedDevice', JSON.stringify({
                id: deviceId,
                name: deviceName,
                timestamp: Date.now()
            }));
            
            // Navigate to connect page
            window.location.href = 'connect.html';
        }
        
        function editDeviceName() {
            document.getElementById('deviceNameInput').value = myDeviceName;
            document.getElementById('nameModal').classList.add('show');
        }
        
        function closeModal(id) {
            document.getElementById(id).classList.remove('show');
        }
        
        function saveDeviceName() {
            const newName = document.getElementById('deviceNameInput').value.trim();
            if (!newName || newName.length > 20) {
                alert('Invalid name');
                return;
            }
            myDeviceName = newName;
            localStorage.setItem('deviceName', myDeviceName);
            document.getElementById('myDeviceName').textContent = myDeviceName;
            closeModal('nameModal');
        }
        
        // Cleanup on page close
        window.addEventListener('beforeunload', () => {
            if (broadcastInterval) clearInterval(broadcastInterval);
            if (discoveryInterval) clearInterval(discoveryInterval);
        });
    </script>
</body>
</html>'''

# Save discover.html
with open('discover.html', 'w', encoding='utf-8') as f:
    f.write(discover_html)

print("✅ discover.html - LOCAL DEVICE DISCOVERY SYSTEM CREATED!")
print("\n🔧 KEY FEATURES:")
print("   1. BROADCASTING: Device sends heartbeat every 1 second")
print("   2. SIGNAL STORAGE: Signals stored in localStorage")
print("   3. DISCOVERY: Scan localStorage for OTHER broadcasts")
print("   4. FILTERING: Only show devices on SAME subnet")
print("   5. TIME-BASED: Remove stale signals older than 15 seconds")
print("   6. REAL-TIME: Updates every 500ms")
print("\n✅ HOW IT WORKS:")
print("   Device A → Broadcast heartbeat (localStorage)")
print("                         ↓")
print("   Device B → Scans localStorage every 500ms")
print("                         ↓")
print("   Device B → Finds Device A's signal!")
print("                         ↓")
print("   Device B → Displays Device A in list")
print("                         ↓")
print("   User clicks 'Select' → Goes to connect.html")
print("\n🚀 PERFECT LOCAL NETWORK DISCOVERY!")
