import { TestBed } from '@angular/core/testing';

import { EvaluationService } from './evaluation.service';

describe('EvaluationService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: EvaluationService = TestBed.get(EvaluationService);
    expect(service).toBeTruthy();
  });
});
