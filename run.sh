#!/bin/bash

set -e


case "$1" in

    "")
        echo "Running install sequence..."
        $0 mkdirs
        $0 copy
        ;;

    mkdirs)
        echo "Making directories..."
        mpremote mkdir apps/ || true
        mpremote mkdir apps/known-error || true
        ;;

    copy)
        echo "Copying app files..."
        mpremote cp app/* :/apps/known-error/
        ;;

    *)
        echo "Unknown command"
        exit 1
        ;;

esac


echo "Done"
