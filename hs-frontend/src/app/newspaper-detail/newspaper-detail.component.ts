import { Component, Input, OnInit } from '@angular/core';
import { SearchService } from "../shared/search.service";
import { ActivatedRoute, Router } from "@angular/router";
import { Newspaper } from "../shared/Newspaper";
import { DomSanitizer, SafeHtml, SafeUrl } from '@angular/platform-browser';


@Component({
  selector: 'hs-newspaper-detail',
  templateUrl: './newspaper-detail.component.html',
  styleUrls: ['./newspaper-detail.component.css'],
  styles: []
})
export class NewspaperDetailComponent implements OnInit {

  newspaper: Newspaper;

  highlightedText: SafeHtml;

  query: string;

  image: SafeUrl;

  constructor (
    private ss: SearchService,
    private route: ActivatedRoute,
    private router: Router,
    private sanitizer: DomSanitizer
  ) {}

  ngOnInit() {
    const params = this.route.snapshot.params;
    this.newspaper = new Newspaper();
    this.newspaper.id = params.id;
    this.newspaper.source = JSON.parse(localStorage.getItem(params.id));
    this.query = decodeURI(localStorage.getItem('query'));
    this.markQueryWords();
    this.loadImage();
  }

  navigateBack() {
    this.router.navigate(['/search'], { queryParams: { q: decodeURI(localStorage.getItem('query'))}});
  }

  markQueryWords() {
    let queryWords = this.query.split(" ");

    console.log(this.newspaper.source.Text);

    let text = ''
    console.log(this.newspaper.source);
    this.newspaper.source.Text.map(
      elem => {
        elem.map(
          elem => {
            let tmp = elem.join(' ')
            text = text.concat(tmp)
            text = text.concat('\n')
          }
        )
        text = text.concat('\n')
      }
    )

    queryWords.map( (value) => {
      text = text.replace(new RegExp(`${value}`, 'gi'), `<span style="background: yellow;">${value}</span>`);
    })
    this.highlightedText = this.sanitizer.bypassSecurityTrustHtml(text);
  }

  loadImage() {
    let d = this.newspaper.source
    this.image = this.sanitizer.bypassSecurityTrustUrl(`http://localhost:5000/image/${d.Year}_${d.Month}_${d.Day}_${d.NewspaperNumber}_${d.Edition}_${d.PageNumber}`);
  }
}
