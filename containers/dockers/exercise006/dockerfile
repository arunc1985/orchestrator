# Use base image py-centos:bases
FROM py-centos:bases
RUN mkdir tests
COPY ./application /tests
RUN ls tests
RUN pip3 install -r tests/requirements
RUN cat tests/flask_app.py
CMD python3 tests/flask_app.py
