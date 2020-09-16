 FROM python:onbuild
 WORKDIR /root/onboarding
 RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
 COPY . /
