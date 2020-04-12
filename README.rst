============================
Scalr Python API Wrapper
============================

.. image:: https://api.codacy.com/project/badge/Grade/c73aa1a661124abc95af293cbd4a2743
   :alt: Codacy Badge
   :target: https://app.codacy.com/manual/Nrupesh29/scalr-api?utm_source=github.com&utm_medium=referral&utm_content=Nrupesh29/scalr-api&utm_campaign=Badge_Grade_Dashboard

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