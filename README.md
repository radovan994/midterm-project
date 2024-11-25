# Breast Cancer Detection - midterm project for ML Zoomcamp 2024 cohort

Breast cancer is a kind of cancer that begins as a growth of cells in the breast tissue.

After skin cancer, breast cancer is the most common cancer diagnosed in women in the United States. But breast cancer doesn't just happen in women. Everyone is born with some breast tissue, so anyone can get breast cancer.

Breast cancer survival rates have been increasing. And the number of people dying of breast cancer is steadily going down. Much of this is due to the widespread support for breast cancer awareness and funding for research.

Advances in breast cancer screening allow healthcare professionals to diagnose breast cancer earlier. Finding the cancer earlier makes it much more likely that the cancer can be cured. 

This project aims to figure how Machine Learning can be used to predict if someone is dead or alive based on certain features and metrics.

## Data used is Seer Breast Cancer Data - Labeled from Kaggle.com



## Instructions on using the repo for prediction:
Build the image using: 

```bash
    docker build -t <name> .
```

This builds the <name> image using our dockerfile on top of some python image in our case svizor/...

We run the image: 

```bach
docker run -it --rm -p 9696:9696 <name>
```

9696:9696 part is for ports in and out explained in the video in deployment part of the course

Then run predict-test.py in another prompt to send customer info to model in docker and interpret the result model outputs. The output is either Dead or Alive for the inputted patient. Feel free to edit the features patient (python dictionary) in the file to your needs

---

### *Dockerfile includes installations of all the necessary libraries, we do not have pipenv file here. If you want you can use the environment.yml file as conda environment.*
### *This runs on gunicorn but we can do it with waitress as well, you can run waitress-server.py and in seperate promt predict-test.py if you want to run it outside docker with waitress*
