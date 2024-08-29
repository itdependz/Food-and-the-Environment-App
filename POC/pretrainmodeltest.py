import torchvision.models as models
import torch
model = models.resnet18(pretrained=False)  # Instantiate the model without pre-trained weights
state_dict = torch.load('./model_e220_v-4.700.pth')
model.load_state_dict(state_dict)
model.eval()
input_tensor = torch.rand(1, 3, 224, 224)

output = model(input_tensor)

# The output has unnormalized scores. To get probabilities, you can run a softmax on it.
print(output)