# utils/images.py
import tkinter as tk
from PIL import Image, ImageGrab

class DrawPanel:
    def __init__(self, width=200, height=200, line_width=14, bg='black', fg='white'):
        self.w = width
        self.h = height
        self.line_width = line_width
        self.bg = bg
        self.fg = fg
        self.root = None
        self.canvas = None
        self._last = None
        self._image = None

    def _paint(self, event):
        if self._last is None:
            self._last = (event.x, event.y)
            return
        x0, y0 = self._last
        x1, y1 = event.x, event.y
        self.canvas.create_line(x0, y0, x1, y1,
                                fill=self.fg, width=self.line_width,
                                capstyle=tk.ROUND, smooth=True)
        self._last = (x1, y1)

    def _reset(self, _event=None):
        self._last = None

    def _finalize(self, _event=None):
        # Captura del área del canvas (requiere permisos de captura en el SO)
        self.canvas.update()
        x = self.canvas.winfo_rootx()
        y = self.canvas.winfo_rooty()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        img = ImageGrab.grab(bbox=(x, y, x1, y1)).convert("L")  # escala de grises
        self._image = img.resize((self.w, self.h))
        self.root.destroy()

    def show(self):
        self.root = tk.Tk()
        self.root.title("Dibuje el dígito. Enter = Finalizar")
        self.canvas = tk.Canvas(self.root, width=self.w, height=self.h,
                                bg=self.bg, highlightthickness=1)
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>", self._paint)
        self.canvas.bind("<ButtonRelease-1>", self._reset)

        btn = tk.Button(self.root, text="Finalizar (Enter)", command=self._finalize)
        btn.pack(pady=6)
        self.root.bind("<Return>", self._finalize)
        self.root.mainloop()

    def get_image(self):
        return self._image
