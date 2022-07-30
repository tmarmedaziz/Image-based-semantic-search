from bs4 import BeautifulSoup


class PinterestScraper:
    def load_images(self):
        html = ''
        with open("images.html", encoding="utf8") as image:
            for line in image.read():
                html += line
        return html

    def parse(self, html):
        content = BeautifulSoup(html, 'html.parser')
        # images = {}
        # for image in content.findAll('img'):
        #     images[image['src']] =  image['alt']
        # images = [image['src'] for image in content.findAll('img')]
        
        print(content.find_all("div", {"class": "Pj7 sLG XiG INd m1e"}))
        # for image in images:
        #     print(image)

    def download_images(self):
        pass

    def run(self):
        html = self.load_images()
        self.parse(html)



if __name__ == '__main__':
    scraper = PinterestScraper()
    scraper.run()

