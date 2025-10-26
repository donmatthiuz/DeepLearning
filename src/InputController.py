import keyboard
import time

class InputController:
    def __init__(self, delay: float = 0.05, verbose: bool = True):
        
        self.delay = delay
        self.verbose = verbose

    def write(self, text: str):
        """Escribe texto como si lo hiciera el teclado"""
        if self.verbose:
            print(f"[InputController] Escribiendo: '{text}'")
        keyboard.write(text, delay=self.delay)

    def press(self, key: str):
        """Presiona una tecla individual"""
        if self.verbose:
            print(f"[InputController] Presionando: {key}")
        keyboard.press(key)
        time.sleep(self.delay)
        keyboard.release(key)

    def enter(self):
        """Presiona Enter"""
        self.press("enter")

    def wait(self, seconds: float):
        """Espera un número de segundos"""
        if self.verbose:
            print(f"[InputController] Esperando {seconds}s...")
        time.sleep(seconds)
