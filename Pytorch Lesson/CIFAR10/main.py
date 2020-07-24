import torch
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision import transforms
from lenet5 import Lenet5
from torch import nn, optim
from ResNet import ResNet18

def main():
    batchsz = 32
    cifar_train = datasets.CIFAR10('cifar', True, transforms.Compose([
        transforms.Resize([32, 32]),
        transforms.ToTensor()
    ]), download=True)
    # 启用多线程DataLoader 同时导入多个图片数据
    cifar_train = DataLoader(cifar_train, batch_size=batchsz, shuffle=True)

    cifar_test = datasets.CIFAR10('cifar', False, transforms.Compose([
        transforms.Resize([32, 32]),
        transforms.ToTensor()
    ]), download=True)
    # 启用多线程DataLoader 同时导入多个图片数据
    cifar_test = DataLoader(cifar_test, batch_size=batchsz, shuffle=True)

    # 设置GPU为运算设备
    torch.cuda.set_device(0)
    device = torch.device('cuda')
    # 生成网络实例 并放在GPU上计算
    #model = Lenet5().to(device)
    model = ResNet18().to(device)
    # 设置loss function 为cross entropy
    criteon = nn.CrossEntropyLoss().to(device)
    # 设置优化器
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    # 将网络信息打印
    print(model)

    # 开始training
    for epoch in range(1000):
        model.train()
        for batchidx, (x, label) in enumerate(cifar_train):
            # x:[b, 3, 32, 32]
            # label: [b]
            # 把x,label放到GPU上运算
            x, label = x.to(device), label.to(device)
            # logits: [b,10]
            # label: [b]
            # 将x放入网络中运算得到 logits
            logits = model(x)
            # loss: tensor scalar
            # 调用cross entropy 计算loss
            loss = criteon(logits, label)

            # backprop 反向传播
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print(epoch, loss.item())
        # 在进行test时不进行dropout
        model.eval()
        with torch.no_grad():
            # test
            total_correct = 0
            total_num = 0
            for x, label in cifar_test:
                # x:[b, 3, 32, 32]
                # label: [b]
                # 把x,label放到GPU上运算
                x, label = x.to(device), label.to(device)
                # logits:[b,10]
                logits = model(x)
                # [b]
                pred = logits.argmax(dim=1)
                # pred compare with label => scalar tensor
                total_correct += torch.eq(pred, label).float().sum().item()
                total_num += x.size(0)
            acc = total_correct / total_num
            print(epoch,acc)


if __name__ == '__main__':
    main()
