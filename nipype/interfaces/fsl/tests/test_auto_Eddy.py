# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.epi import Eddy

def test_Eddy_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    flm=dict(argstr='--flm=%s',
    ),
    fwhm=dict(argstr='--fwhm=%s',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_acqp=dict(argstr='--acqp=%s',
    mandatory=True,
    ),
    in_bval=dict(argstr='--bvals=%s',
    mandatory=True,
    ),
    in_bvec=dict(argstr='--bvecs=%s',
    mandatory=True,
    ),
    in_file=dict(argstr='--imain=%s',
    mandatory=True,
    ),
    in_index=dict(argstr='--index=%s',
    mandatory=True,
    ),
    in_mask=dict(argstr='--mask=%s',
    mandatory=True,
    ),
    in_topup=dict(argstr='--topup=%s',
    ),
    method=dict(argstr='--resamp=%s',
    ),
    niter=dict(argstr='--niter=%s',
    ),
    out_base=dict(argstr='--out=%s',
    ),
    output_type=dict(),
    repol=dict(argstr='--repol',
    ),
    session=dict(argstr='--session=%s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    )
    inputs = Eddy.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_Eddy_outputs():
    output_map = dict(out_corrected=dict(),
    out_parameter=dict(),
    )
    outputs = Eddy.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

