FROM svizor/zoomcamp-model:3.11.5-slim


WORKDIR /app


RUN pip install numpy scikit-learn Flask requests gunicorn

COPY ["predict.py","model_C=1.0.bin", "./"]

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "predict:app" ]