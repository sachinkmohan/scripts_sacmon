- Saving and loading a numpy array

```
out = mi.inference(engine_path,  im3, batch_size1)
y_pred = np.reshape(out, (1,-1, 18))

np.save('array_jetson.npy', y_pred)  ## Saves a .npy file
y_pred_load = np.load('array_ssd7_pc.npy')  ## Loads the .npy file
```

