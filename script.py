
# Create a multi-page application structure with separate HTML files

# 1. Main index.html - Home/Landing page
index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LocalDrop - Instant File Sharing</title>
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
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 24px;
            padding: 48px;
            max-width: 600px;
            width: 100%;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            text-align: center;
        }
        
        h1 {
            font-size: 48px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 16px;
        }
        
        .tagline {
            font-size: 20px;
            color: #6b7280;
            margin-bottom: 40px;
        }
        
        .features {
            text-align: left;
            margin: 40px 0;
        }
        
        .feature {
            display: flex;
            align-items: center;
            margin: 16px 0;
            padding: 16px;
            background: #f9fafb;
            border-radius: 12px;
        }
        
        .feature-icon {
            font-size: 32px;
            margin-right: 16px;
        }
        
        .feature-text h3 {
            font-size: 18px;
            margin-bottom: 4px;
        }
        
        .feature-text p {
            font-size: 14px;
            color: #6b7280;
        }
        
        .cta-buttons {
            display: flex;
            gap: 16px;
            justify-content: center;
            margin-top: 40px;
        }
        
        .btn {
            padding: 16px 32px;
            border: none;
            border-radius: 12px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        
        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        
        .btn-secondary {
            background: #f3f4f6;
            color: #1f2937;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }
        
        .footer {
            margin-top: 48px;
            padding-top: 32px;
            border-top: 2px solid #f3f4f6;
            color: #6b7280;
        }
        
        .footer strong {
            color: #ef4444;
        }
        
        @media (max-width: 768px) {
            .container {
                padding: 32px;
            }
            
            h1 {
                font-size: 36px;
            }
            
            .cta-buttons {
                flex-direction: column;
            }
            
            .btn {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 LocalDrop</h1>
        <p class="tagline">Instant File Sharing - No Setup Required</p>
        
        <div class="features">
            <div class="feature">
                <div class="feature-icon">📱</div>
                <div class="feature-text">
                    <h3>Cross-Platform</h3>
                    <p>Works on iOS, Android, Windows, Mac, Linux</p>
                </div>
            </div>
            
            <div class="feature">
                <div class="feature-icon">🔒</div>
                <div class="feature-text">
                    <h3>Secure & Private</h3>
                    <p>Direct P2P transfer, files never touch our servers</p>
                </div>
            </div>
            
            <div class="feature">
                <div class="feature-icon">⚡</div>
                <div class="feature-text">
                    <h3>Lightning Fast</h3>
                    <p>Transfer files at maximum local network speed</p>
                </div>
            </div>
            
            <div class="feature">
                <div class="feature-icon">📷</div>
                <div class="feature-text">
                    <h3>QR Code Connect</h3>
                    <p>Scan QR codes for instant device connection</p>
                </div>
            </div>
        </div>
        
        <div class="cta-buttons">
            <a href="connect.html" class="btn btn-primary">🚀 Start Sharing</a>
            <a href="discover.html" class="btn btn-secondary">🔍 Discover Devices</a>
        </div>
        
        <div class="footer">
            <p>Made with <strong>❤️</strong> in India by <strong>PROGRAMMER MJ</strong></p>
            <p style="margin-top: 8px; font-size: 14px;">LocalDrop v2.0.0</p>
        </div>
    </div>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("✅ index.html created - Landing page")
