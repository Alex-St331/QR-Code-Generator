import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import ImageTk, Image
from io import BytesIO

def generate_qr():
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(entry.get())
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    
    # Convert PIL Image to Tkinter PhotoImage and show it on the label
    global photo
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)

    # Save the PIL image in memory for saving to file later
    global qr_img
    qr_img = img

def save_qr():
    if qr_img is None:
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    if file_path:
        qr_img.save(file_path)

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create the input field
entry = tk.Entry(root)
entry.pack()

# Create the QR code display label
photo = None
label = tk.Label(root)
label.pack()

# Create the generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack()

# Create the save button
qr_img = None
save_button = tk.Button(root, text="Save QR Code", command=save_qr)
save_button.pack()

root.mainloop()
