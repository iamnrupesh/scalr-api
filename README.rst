============================
Scalr Python API Wrapper
============================

Install
-------
.. code-block:: console

   $ pip install scalr-api

Examples
--------

Here is an example of how to delete a Scalr role:

.. code-block:: python

    from scalr import ScalrUserAPI

    scalr = ScalrUserAPI(
                url='https://your-scalr-host/',
                key_id='your_scalr_key_id',
                secret_key='your_scalr_secret_key',
                env_id=your_scalr_environment_id
            )

    scalr.role_delete(role_id=your_role_id)

Credits
-------

* Scalr_ for providing examples on how to use Scalr API v2.

.. _Scalr: https://github.com/scalr-tutorials/apiv2-examples