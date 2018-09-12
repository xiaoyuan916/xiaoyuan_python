import pygame


def main():
    # 初始化
    pygame.init()
    # 设置窗口
    screen = pygame.display.set_mode((800, 600))
    # 设置窗口标题
    pygame.display.set_caption("pygame")
    running = True
    # 开启一个事件
    while running:
        # 消息队列中获取事件并处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
