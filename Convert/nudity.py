import coremltools

coreml_model = coremltools.converters.caffe.convert(('resnet_50_1by2_nsfw.caffemodel', 'deploy.prototxt'), image_input_names='data', red_bias=-104, green_bias=-117, blue_bias=-123, is_bgr=True, class_labels='labels.txt')
coreml_model.author = 'Philipp Gabriel'
coreml_model.license = 'BSD-2'
coreml_model.short_description = 'Classifies an image either as NSFW (nude) or SFW (not nude)'
coreml_model.input_description['data'] = 'Image used for classification'
coreml_model.output_description['classLabel'] = 'NSFW or SFW'
coreml_model.output_description['prob'] = 'Probabilities of classes'
coreml_model.save('Nudity.mlmodel')
