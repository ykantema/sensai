 FROM python:onbuild
 WORKDIR /root/onboarding
 COPY requirements.txt ./
 RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
 COPY . /
