import { Component, Input, OnInit } from '@angular/core';
import { SearchService } from "../shared/search.service";
import { ActivatedRoute, Router } from "@angular/router";
import { Newspaper } from "../shared/Newspaper";

@Component({
  selector: 'hs-newspaper-detail',
  templateUrl: './newspaper-detail.component.html',
  styleUrls: ['./newspaper-detail.component.css'],
  styles: []
})
export class NewspaperDetailComponent implements OnInit {

  newspaper: Newspaper;

  constructor (
    private ss: SearchService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit() {
    const params = this.route.snapshot.params;
    this.newspaper = new Newspaper();
    this.newspaper.id = params.id;
    this.newspaper.source = JSON.parse(localStorage.getItem(params.id));
  }

  navigateBack() {
    this.router.navigate(['/search'], { queryParams: { q: localStorage.getItem('query')}});
  }
}
