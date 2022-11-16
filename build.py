from setuptools import Extension


ext = Extension(
    name="jdsetup.gs3.fdshape.encoder",
    sources=["jdsetup/gs3/fdshape/encoder.c"],
    define_macros=[("PY_SSIZE_T_CLEAN",)],
    include_dirs=["$PYTHONPATH"],
    library_dirs=["$LIB"],
    libraries=["python3"],
)

def build(setup_kwargs):
    """
    This is a callback for poetry used to hook in our extensions.
    """

    setup_kwargs.update(
        {
            # declare the extension so that setuptools will compile it
            "ext_modules": [ext],
        }
    )

