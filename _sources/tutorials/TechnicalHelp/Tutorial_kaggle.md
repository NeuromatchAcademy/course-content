# Using Kaggle

If you are in China or another region with difficult  access to Google Colab, you can use Kaggle as a substitute for launching an interactive coding environment where you can write and run code. Please note that we recommend Google colab if you can access it.

## STEPS:

**1.** First, [sign in](https://www.kaggle.com/account/login) to your Kaggle account. If you don't have a Kaggle account, create one by registering for it by clicking [here](https://www.kaggle.com/account/login?phase=startRegisterTab&returnUrl=%2F). 
![Step 1](../static/kaggle_step1.png)

**2.** Once you're logged into your account, click the kaggle button found on top of every page containing a tutorial.
![Step 2](../static/kaggle_step2.png)

>**NOTE:-** In case that you inspect an error asocociated with `!pip install` then follow [this workaround](https://www.kaggle.com/product-feedback/63544).

**3.**  First time users have get their phone numbers verified. In order to have GPU/internet access, on the left sidebar of the notebook under the settings panel, go to **Get phone verified** link and enter your credentials.

![Step 3.1](../static/kaggle_step6_1.png)

Go to *Settings* -> *Internet* and select *Internet connected*. Your Kernels session restarts and the newly started session is enabled to access the Internet. If after the installation you experience any error when trying to import an installed module, make sure to restart the kernel after installing the module and then it should work.

![Step 3.2](../static/kaggle_internet_enabled.png)

>**NOTE:-** The last step, that is **step 4** grants you access to GPU in Kaggle. It is **NOT** required for Computational Neuroscience course and is only required for Deep Learning course

**4.** (Optional) The last and final step about how to leverage **GPU** accelerator in the kaggle kernel. You should not need to do this ever for the comp neuro course tutorials. You may want it for project work and especially for the deep learning course.

Once your phone number has been verified, on the left sidebar under **Settings** panel, select **Accelerator** to **GPU** from **None** using the drop down menu.

![Step 4.1](../static/kaggle_step6_2.png)
