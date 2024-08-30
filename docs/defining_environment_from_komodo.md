# How to create your own virtual environment based on Komodo

Information can be found on <br>
https://github.com/equinor/komodoenv

1. Source Komodo environment<br>
`source /prog/res/komodo/stable/enable.csh`
2. Create a personnal duplicate of the environment (it does not have to be named my-kenv)<br>
`komodoenv my-kenv`
2. Create a personnal duplicate of the environment<br>
`komodoenv geostats-kenv`
3. source the new environment<br>
`source my-kenv/enable.csh`   (my-kenv/enable, depending on your configuration)
4. install whatever required packages that are not covered by komodo<br>
`pip install geostatspy`

Next step is to install the new environment in a python kernel<br>
`python -m ipykernel install --user --name=my-kenv --display-name="Python (geostats-kenv)"`

NB: be aware that update of your environment is not automatic and it should be frequently updated (especially with new komodo release) by<br>
`komodoenv-update`
NB2: each new terminal windows will start with the default komodo. You will have to source your own vitual environment.


# Using that new environment 
We will use GeostatGuy notebook for that
1. create a new folder on your users where to store the notebook<br>
`mkdir GeostatGuy`
2. cloning the original notebook <br>
`cd GeostatGuy` <br>
`git clone https://github.com/GeostatsGuy/GeostatsPyDemos_Book.git`
3. start jupyter-lab and be ready to ~~cry~~ play<br>
`jupyter-lab`
4. Select the kernel <br> 
kernel>Change_kernel <br>
select the newly created one.

Ready to test ? Run the 1st block (CTRl+ENTER). If failing on import, install the required package and reload kernel,test again.
