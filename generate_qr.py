import os
import qrcode

# Get environment variables or use defaults
data_url = os.getenv("QR_DATA_URL", "https://github.com/henip1234")
output_dir = os.getenv("QR_CODE_DIR", "qr_codes")
filename = os.getenv("QR_CODE_FILENAME", "github_qr.png")
fill_color = os.getenv("FILL_COLOR", "black")
back_color = os.getenv("BACK_COLOR", "white")

# Create directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Create QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(data_url)
qr.make(fit=True)

img = qr.make_image(fill_color=fill_color, back_color=back_color)

# Save image
output_path = os.path.join(output_dir, filename)
img.save(output_path)

print(f"✅ QR code saved to: {output_path}")
print(f"📎 Points to: {data_url}")
