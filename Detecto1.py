
from detecto import core, utils, visualize

image = utils.read_image('E:\\Spritle\\Code\\fruit.jpg')
model = core.Model()

labels, boxes, scores = model.predict_top(image)
visualize.show_labeled_image(image, boxes, labels)
