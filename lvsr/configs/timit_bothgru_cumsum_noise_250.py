
Config(
    net=Config(
        dim_dec=250,
        dim_bidir=250,
        dims_bottom=[250],
        dec_transition='GatedRecurrent',
        enc_transition='GatedRecurrent',
        attention_type='content_and_cumsum'),
    initialization=[
        ("/recognizer", "rec_weights_init", "IsotropicGaussian(0.1)")],
    regularization=Config(
        noise=0.075),
    data=Config(
        normalization="norm.pkl"))
