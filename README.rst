========================
Scalr Python API Wrapper
========================

.. image:: https://badge.fury.io/py/scalr-api.svg
    :target: https://badge.fury.io/py/scalr-api
.. image:: https://img.shields.io/pypi/l/scalr-api.svg
    :target: https://pypi.python.org/pypi/scalr-api/
.. image:: https://api.codacy.com/project/badge/Grade/c73aa1a661124abc95af293cbd4a2743
   :target: https://app.codacy.com/manual/Nrupesh29/scalr-api?utm_source=github.com&utm_medium=referral&utm_content=Nrupesh29/scalr-api&utm_campaign=Badge_Grade_Dashboard

Install
-------

.. code-block:: console

   $ pip install scalr-api


Examples
--------

Here are some examples on how to work with Scalr roles:

.. code-block:: python

    from scalr import ScalrUserAPI

    scalr = ScalrUserAPI(
                url='https://your-scalr-host/',
                key_id='your_scalr_key_id',
                secret_key='your_scalr_secret_key',
                env_id=4
            )
    
    role_data = {
      "builtinAutomation": [
        "base"
      ],
      "category": {
        "id": 1
      },
      "name": "string",
      "os": {
        "id": "string"
      },
      "useScalrAgent": true
    }
 
    scalr.role_create(role=role_data)
    scalr.role_delete(role_id=12)
    
    updated_role_data = {
      "category": {
        "id": 1
      },
      "description": "string",
      "name": "string",
      "quickStart": true,
      "quickStartGroup": "string",
      "tags": [
        "string"
      ]
    }
    
    scalr.role_edit(role_id=26, role=updated_role_data)
    role = scalr.role_get(role_id=9)
    roles = scalr.role_list()
    scalr.role_clone(role_id=45, name="Cloned Role")


Credits
-------

* Scalr_ for providing examples on how to use Scalr API v2.

.. _Scalr: https://github.com/scalr-tutorials/apiv2-examples
