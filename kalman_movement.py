import numpy as np

acc = 2  # 2m/s2
delT = 1  # seconds

delX = 20
delV = 5

X_input = np.array([[4000, 280]])

pc = np.array([[delX * delX, delX * delV], [delX * delV, delV * delV]])

A_matrix = np.array([[1, 0], [delT, 1]])

B_matrix = np.array([0.2 * delT * delT, delT])

X_obs = [4260, 4550, 4860, 5110]
V_obs = [282, 285, 286, 290]
R_obs = np.array([[25 * 25, 25 * 6], [25 * 6, 36]])
pc_pred = pc

for i in range(len(X_obs)):
    X_pred = np.add(np.dot(X_input, A_matrix), B_matrix * acc)
    K = np.divide(pc_pred, (pc_pred + R_obs)) # Kalman Gain
    y_pred = np.array([X_obs[i], V_obs[i]])
    print(y_pred)

    x_final = X_pred + np.dot(K, (np.subtract(y_pred, X_pred)).T).T
    print(x_final)

    X_input = x_final
    pc_pred = (np.dot(np.subtract([[1,0],[0,1]], K), pc_pred))