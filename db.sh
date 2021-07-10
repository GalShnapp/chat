#!/bin/bash

POSTGRES_PASSWORD="password"


docker run --name postgres_0 -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD -d -p 5432:5432 postgres:alpine 