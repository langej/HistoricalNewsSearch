import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {SearchService} from "../shared/search.service";
import {Newspaper} from "../shared/Newspaper";
import { EvaluationService } from '../shared/evaluation.service';
import { EvaluationElement } from '../shared/EvaluationElement';
import {filter} from "rxjs/operators";

@Component({
  selector: 'hs-result-list',
  templateUrl: './result-list.component.html',
  styleUrls: ['./result-list.component.css'],
  providers: [SearchService, EvaluationService]
})
export class ResultListComponent implements OnInit {

  page: number = 1;
  newspapers: Newspaper[];
  displayEvaluation: boolean = true;

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private searchService: SearchService,
    private evaluationService: EvaluationService
  ) {}

  ngOnInit() {
    if (this.route.snapshot.queryParamMap.get('eval')) {
      this.displayEvaluation = true;
    }
    this.router.routeReuseStrategy.shouldReuseRoute = () => false;
    this.newspapers = new Array<Newspaper>();
    if (this.router.url !== '/search') {
      const url = this.cleanUrl();
      this.searchService.getSearchResults(url).then( (results) => {
        results.map( (data) => {
          this.newspapers.push(data);
        });
      });
    }
  }

  private cleanUrl() {
    let url = this.router.url.split('?q=')[1];
    url = url.replace(/%20/g, ' ');
    return url;
  }

  postEvaluation() {
    const evaluationData = new Array<EvaluationElement>();
    const border = this.newspapers.length <= 10 ? this.newspapers.length : 10;
    for (let index = 0; index < border; index++) {
      const tmp: EvaluationElement = JSON.parse(localStorage.getItem(`evaluation-${index}`));
      if (tmp.evaluated === false) {
        break;
      } else {
        evaluationData.push({
          id: tmp.id,
          index: tmp.index,
          relevant: tmp.relevant
        });
      }
    }
    this.evaluationService.postEvaluation(evaluationData);
  }
}
