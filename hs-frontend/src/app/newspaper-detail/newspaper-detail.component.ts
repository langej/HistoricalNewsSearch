import { Component, Input, OnInit } from '@angular/core';
import { SearchService } from "../shared/search.service";
import { ActivatedRoute, Router } from "@angular/router";
import { Newspaper } from "../shared/Newspaper";
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';

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
  }

  navigateBack() {
    this.router.navigate(['/search'], { queryParams: { q: decodeURI(localStorage.getItem('query'))}});
  }

  markQueryWords() {
    let queryWords = this.query.split(" ");

    let text: string = this.newspaper.source.Text;

    queryWords.map( (value) => {
      text = text.replace(new RegExp(`${value}`, 'gi'), `<span class="marked">${value}</span>`);
    })
    this.highlightedText = this.sanitizer.bypassSecurityTrustHtml(text);
  }
}
