import numpy as np

def grad(f, x, h=1e-7):
    """Calcula el gradiente de la función f en el punto x"""
    grad = np.zeros_like(x)
    for i in range(x.size):
        x_plus, x_minus = x.copy(), x.copy()
        x_plus[i] += h
        x_minus[i] -= h
        grad[i] = (f(x_plus) - f(x_minus)) / (2 * h)
    return grad

def bb_step(x, x_prev, grad, grad_prev):
    """Calcula el paso de Barzilai-Borwein"""
    s = x - x_prev
    y = grad - grad_prev
    t = np.dot(s, y) / np.dot(y, y)
    return t

def grad_desc_bb(f, x0, tol=1e-6, max_iter=10000):
    """Realiza el gradiente descendente con el paso de Barzilai-Borwein"""
    x = x0
    x_prev = x0
    grad_prev = grad(f, x)
    for _ in range(max_iter):
        grad_cur = grad(f, x)
        if np.linalg.norm(grad_cur) < tol:
            break
        if _ > 0: # BB step is undefined for the first step
            t = bb_step(x, x_prev, grad_cur, grad_prev)
        else:
            t = 1e-3 # Initial step size
        x_prev = x
        grad_prev = grad_cur
        x = x - t * grad_cur
    return x

# Ejemplo de uso
def f(x):
    return x[0]**2 + 2 * x[1]**2 # función objetivo

x0 = np.array([2.0, 3.0]) # punto inicial
opt_x = grad_desc_bb(f, x0)

print("El óptimo se encuentra en", opt_x)