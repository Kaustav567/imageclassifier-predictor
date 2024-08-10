{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1774b05e-32dd-4424-b1d5-0f2a4302fa00",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "An error occurred: in user code:\n",
      "\n",
      "    File \"C:\\Users\\KIIT\\Documents\\machproj\\envs\\machproj\\lib\\site-packages\\keras\\engine\\training.py\", line 2169, in predict_function  *\n",
      "        return step_function(self, iterator)\n",
      "    File \"C:\\Users\\KIIT\\Documents\\machproj\\envs\\machproj\\lib\\site-packages\\keras\\engine\\training.py\", line 2155, in step_function  **\n",
      "        outputs = model.distribute_strategy.run(run_step, args=(data,))\n",
      "    File \"C:\\Users\\KIIT\\Documents\\machproj\\envs\\machproj\\lib\\site-packages\\keras\\engine\\training.py\", line 2143, in run_step  **\n",
      "        outputs = model.predict_step(data)\n",
      "    File \"C:\\Users\\KIIT\\Documents\\machproj\\envs\\machproj\\lib\\site-packages\\keras\\engine\\training.py\", line 2111, in predict_step\n",
      "        return self(x, training=False)\n",
      "    File \"C:\\Users\\KIIT\\Documents\\machproj\\envs\\machproj\\lib\\site-packages\\keras\\utils\\traceback_utils.py\", line 70, in error_handler\n",
      "        raise e.with_traceback(filtered_tb) from None\n",
      "    File \"C:\\Users\\KIIT\\Documents\\machproj\\envs\\machproj\\lib\\site-packages\\keras\\engine\\input_spec.py\", line 298, in assert_input_compatibility\n",
      "        raise ValueError(\n",
      "\n",
      "    ValueError: Input 0 of layer \"sequential\" is incompatible with the layer: expected shape=(None, 32, 32, 3), found shape=(None, 224, 224, 3)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import filedialog\n",
    "from PIL import Image, ImageTk\n",
    "import numpy as np\n",
    "import tensorflow as tf\n",
    "\n",
    "# Load your model\n",
    "model = tf.keras.models.load_model('imgclassifier.keras')\n",
    "\n",
    "def open_file():\n",
    "    try:\n",
    "        file_path = filedialog.askopenfilename(filetypes=[(\"Image files\", \".jpg;.jpeg;*.png\")])\n",
    "        if file_path:\n",
    "            image = Image.open(file_path)\n",
    "            photo = ImageTk.PhotoImage(image)\n",
    "            label.config(image=photo)\n",
    "            label.image = photo\n",
    "\n",
    "            # Preprocess the image\n",
    "            image = image.resize((224, 224))\n",
    "            image = np.array(image) / 255.0\n",
    "            image = np.expand_dims(image, axis=0)\n",
    "\n",
    "            # Make predictions\n",
    "            predictions = model.predict(image)\n",
    "            print(predictions)\n",
    "    except Exception as e:\n",
    "        print(f\"An error occurred: {e}\")\n",
    "\n",
    "# Create main window\n",
    "root = tk.Tk()\n",
    "root.title(\"Image Classifier\")\n",
    "\n",
    "# Add GUI elements\n",
    "open_button = tk.Button(root, text=\"Open Image\", command=open_file)\n",
    "open_button.pack(pady=20)\n",
    "\n",
    "label = tk.Label(root)\n",
    "label.pack()\n",
    "\n",
    "# Start the GUI event loop\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31b17551-44fa-4fd5-9cf9-1ee2f57b5d38",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "437d6f0b-7400-499c-ad12-cb380d847353",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
