Neural Enhance
==============

`As seen on TV! <https://www.youtube.com/watch?v=LhF_56SxrGk>`_ What if you could increase the resolution of your photos using technology from CSI laboratories? Thanks to deep learning, it's now possible to train a neural network to zoom in to your images using examples.  You'll get better results by increasing the number of neurons and specializing the training images (e.g. faces).

The catch? The neural network is hallucinating details based on its training from example images. It's not reconstructing the image exactly as it would have been if it was HD. That's only possible in Holywood — but deep learning as "Creative AI" works and its just as cool!  Here's how you can get started...

1. `Examples & Usage <#1-examples--usage>`_
2. `Installation <#2-installation--setup>`_
3. `Background & Research <#3-background--research>`_
4. `Troubleshooting <#4-troubleshooting-problems>`_
5. `Frequent Questions <#5-frequent-questions>`_

|Python Version| |License Type| |Project Stars|

----

1. Examples & Usage
===================

The main script is called ``enhance.py``, which you can run with Python 3.4+ (see setup below).  The ``--device`` argument that lets you specify which GPU or CPU to use. For the samples above, here are the performance results:

* **GPU Rendering** — Assuming you have CUDA setup and enough on-board RAM to fit the image and neural network, generating 1080p output should complete in 5 seconds.
* **CPU Rendering** — This will take roughly 20 seconds for 1080p output, however on most machines you can run 4-8 processes simultaneously given enough system RAM.

The default is to use ``cpu``, if you have NVIDIA card setup with CUDA already try ``gpu0``. On the CPU, you can also set environment variable to ``OMP_NUM_THREADS=4``, but we've found the speed improvements to be minimal.


1.a) Enhancing Images
---------------------

.. code:: bash

    python3 enhance.py

1.b) Training Super-Resolution
------------------------------

.. code:: bash

    rm -f ne4x.pkl.bz2

    python3.4 enhance.py --train --epochs=25 \
              --scales=2 --perceptual-layer=conv2_2 \
              --generator-block=16 --generator-filters=128 \
              --smoothness-weight=1e7 --adversary-weight=0.0

    python3.4 enhance.py --train --epochs=250 \
              --scales=2 --perceptual-layer=conv5_2 \
              --smoothness-weight=5e4 --adversary-weight=2e2 \
              --generator-start=1 --discriminator-start=0 --adversarial-start=1


2. Installation & Setup
=======================

2.a) Using Docker Image [recommended]
-------------------------------------

The easiest way to get up-and-running is to `install Docker <https://www.docker.com/>`_. Then, you should be able to downloand and run the pre-built image using the ``docker`` command line tool.  Find out more about the ``alexjc/neural-enhance`` image on its `Docker Hub <https://hub.docker.com/r/alexjc/neural-enhance/>`_ page.

The easiest way to run the script from the docker image is to setup an easy access command called `enhance`. This will automatically:

* Mount the ``frames`` folder from current directory into the instance for visualization.
* Expose the ``samples`` folder from the current directory so the script can access files!

This is how you can do it in your terminal console on OSX or Linux:

.. code:: bash

    # Setup the alias. Put this in your .bash_rc or .zshrc file so it's available at startup.
    alias enhance="docker run -v $(pwd)/samples:/ne/samples -it alexjc/neural-enhance"
    
    # Now run any of the examples above using this alias, without the `.py` extension.
    enhance --help

If you want to run on your NVIDIA GPU, you can instead use the image ``alexjc/neural-enhance:gpu`` which comes with CUDA and CUDNN pre-installed in the image.  See the scripts in ``docker/*.sh`` for how to setup your host machine. (advanced)


2.b) Manual Installation [developers]
-------------------------------------

This project requires Python 3.4+ and you'll also need ``numpy`` and ``scipy`` (numerical computing libraries) as well as ``python3-dev`` installed system-wide.  If you want more detailed instructions, follow these:

1. `Linux Installation of Lasagne <https://github.com/Lasagne/Lasagne/wiki/From-Zero-to-Lasagne-on-Ubuntu-14.04>`_ **(intermediate)**
2. `Mac OSX Installation of Lasagne <http://deeplearning.net/software/theano/install.html#mac-os>`_ **(advanced)**
3. `Windows Installation of Lasagne <https://github.com/Lasagne/Lasagne/wiki/From-Zero-to-Lasagne-on-Windows-7-%2864-bit%29>`_ **(expert)**

Afterward fetching the repository, you can run the following commands from your terminal to setup a local environment:

.. code:: bash

    # Create a local environment for Python 3.x to install dependencies here.
    python3 -m venv pyvenv --system-site-packages

    # If you're using bash, make this the active version of Python.
    source pyvenv/bin/activate

    # Setup the required dependencies simply using the PIP module.
    python3 -m pip install --ignore-installed -r requirements.txt

After this, you should have ``pillow``, ``theano`` and ``lasagne`` installed in your virtual environment.  You'll also need to download this `pre-trained neural network <https://github.com/alexjc/neural-doodle/releases/download/v0.0/vgg19_conv.pkl.bz2>`_ (VGG19, 80Mb) and put it in the same folder as the script to run. To de-install everything, you can just delete the ``#/pyvenv/`` folder.


3. Background & Research
========================

1. `Perceptual Losses for Real-Time Style Transfer and Super-Resolution <http://arxiv.org/abs/1603.08155>`_
2. `Real-Time Super-Resolution Using Efficient Sub-Pixel Convolution <https://arxiv.org/abs/1609.05158>`_
3. `Deeply-Recursive Convolutional Network for Image Super-Resolution <https://arxiv.org/abs/1511.04491>`_
4. `Photo-Realistic Super-Resolution Using a Generative Adversarial Network <https://arxiv.org/abs/1609.04802>`_


4. Troubleshooting Problems
===========================

Can't install or Unable to find pgen, not compiling formal grammar.
-------------------------------------------------------------------

There's a Python extension compiler called Cython, and it's missing or inproperly installed. Try getting it directly from the system package manager rather than PIP.

**FIX:** ``sudo apt-get install cython3``


NotImplementedError: AbstractConv2d theano optimization failed.
---------------------------------------------------------------

This happens when you're running without a GPU, and the CPU libraries were not found (e.g. ``libblas``).  The neural network expressions cannot be evaluated by Theano and it's raising an exception.

**FIX:** ``sudo apt-get install libblas-dev libopenblas-dev``


TypeError: max_pool_2d() got an unexpected keyword argument 'mode'
------------------------------------------------------------------

You need to install Lasagne and Theano directly from the versions specified in ``requirements.txt``, rather than from the PIP versions.  These alternatives are older and don't have the required features.

**FIX:** ``python3 -m pip install -r requirements.txt``


ValueError: unknown locale: UTF-8
---------------------------------

It seems your terminal is misconfigured and not compatible with the way Python treats locales. You may need to change this in your ``.bash_rc`` or other startup script. Alternatively, this command will fix it once for this shell instance.

**FIX:** ``export LC_ALL=en_US.UTF-8``


5. Frequent Questions
=====================

Q: Is there an application for this? I want to download it!
-----------------------------------------------------------

A: Not yet.


----

|Python Version| |License Type| |Project Stars|

.. |Python Version| image:: http://aigamedev.github.io/scikit-neuralnetwork/badge_python.svg
    :target: https://www.python.org/

.. |License Type| image:: https://img.shields.io/badge/license-AGPL-blue.svg
    :target: https://github.com/alexjc/neural-enhance/blob/master/LICENSE

.. |Project Stars| image:: https://img.shields.io/github/stars/alexjc/neural-enhance.svg?style=flat
    :target: https://github.com/alexjc/neural-enhance/stargazers