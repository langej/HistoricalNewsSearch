import { Component, Input, OnInit } from '@angular/core';
import { SearchService } from "../shared/search.service";
import { ActivatedRoute } from "@angular/router";
import { Newspaper } from "../shared/Newspaper";

@Component({
  selector: 'hs-newspaper-detail',
  templateUrl: './newspaper-detail.component.html',
  styles: []
})
export class NewspaperDetailComponent implements OnInit {

  @Input()
  newspaper: Newspaper;

  constructor (
    private ss: SearchService,
    private route: ActivatedRoute
  ) {}

  ngOnInit() {
    const params = this.route.snapshot.params;
    this.newspaper = JSON.parse(localStorage.getItem(params.id));
  }
}
